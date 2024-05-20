# ライブラリのインポート
import sys
import requests
import json
import re
import csv
from datetime import datetime
from dateutil import tz

token = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
# token = os.environ['GITHUB_TOKEN']

# リポジトリの情報
organization = "YOUR_ORGANIZATION"
repository = "YOUR_REPOSITORY"

# APIのURL
url = f"https://api.github.com/repos/{organization}/{repository}/issues"

# parameters
params = "?state=all&per_page=100&page=1"

# request header
headers = {"Authorization": f"token {token}"}


def tz_trans(z_str):
    if not z_str:
        return ""

    utc_str = z_str.replace("Z", " UTC")
    utc = datetime.strptime(utc_str, "%Y-%m-%dT%H:%M:%S %Z")
    from_zone = tz.gettz("UTC")
    to_zone = tz.gettz("Asia/Tokyo")
    local_tm = utc.replace(tzinfo=from_zone).astimezone(to_zone)
    return local_tm.strftime("%Y-%m-%d %H:%M:%S")


def to_csv(headlist, rows):
    writer = csv.writer(sys.stdout)

    # header
    writer.writerow(headlist)

    # columns
    for row in rows:
        col = []
        for head in headlist:
            col.append(row[head] if head in row else "")

        writer.writerow(col)


def main():
    # リクエストの実行
    response = requests.get(url + params, headers=headers)

    # ステータスコードの確認
    if response.status_code == 200:
        # JSON形式のデータをパース
        data = json.loads(response.text)

        # Issueの情報を表示
        heads = set()
        rows = []

        for issue in data:
            row = {}
            row["1.title"] = issue["title"]
            row["2.state"] = issue["state"]

            assignees = {}
            if issue["assignees"]:
                assignees = [x["login"] for x in issue["assignees"]]
            row["3.assignees"] = "&".join(assignees)

            row["4.body"] = issue["body"]
            row["5.created_at"] = tz_trans(issue["created_at"])
            row["6.updated_at"] = tz_trans(issue["updated_at"])
            row["7.closed_at"] = tz_trans(issue["closed_at"])
            row["8.url"] = issue["url"]

            labels = []
            for label in issue["labels"]:
                lname = label["name"]
                elif "bug" in lname:
                    row["B.bug"] = "○"
                elif "func:" in lname:
                    row[lname] = "○"
                elif re.search(
                    "(view|api)", lname
                ):
                    row["c:" + lname] = "○"
                else:
                    # print(lname)
                    labels.append(lname)
                    row["othre_labels"] = "&".join(labels)

            # print(row)
            heads = heads.union(key for key in row)
            rows.append(row)

        # output
        headlist = sorted(list(heads))
        to_csv(headlist, rows)

    else:
        # エラー処理
        print(f"エラーが発生しました: {response.status_code}")


if __name__ == "__main__":
    main()
