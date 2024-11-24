import React, { useEffect, useRef, useState } from "react";
import Avatar from "@mui/material/Avatar";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemAvatar from "@mui/material/ListItemAvatar";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";
import DialogTitle from "@mui/material/DialogTitle";
import Dialog from "@mui/material/Dialog";
import { blue } from "@mui/material/colors";
import DescriptionOutlinedIcon from "@mui/icons-material/DescriptionOutlined";
import mapboxgl from "mapbox-gl";
import "mapbox-gl/dist/mapbox-gl.css";

const DialogTest = () => {
  const mapContainerRef = useRef();
  const mapRef = useRef();

  const [open, setOpen] = useState(false);
  const [dataList, setDataList] = useState([]);

  useEffect(() => {
    mapboxgl.accessToken = process.env.REACT_APP_MAPBOX_ACCESS_TOKEN;

    mapRef.current = new mapboxgl.Map({
      container: mapContainerRef.current,
      center: [135.5, 35],
      zoom: 5,
    });

    mapRef.current.on("load", () => {
      mapRef.current.addSource("earthquakes", {
        type: "geojson",
        data: "https://docs.mapbox.com/mapbox-gl-js/assets/earthquakes.geojson",
      });

      mapRef.current.addLayer({
        id: "earthquakes-layer-base",
        type: "symbol",
        source: "earthquakes",
        layout: {
          "text-field": "●",
          "text-size": 30,
          "text-allow-overlap": true,
        },
        paint: {
          "text-color": "magenta",
          "text-opacity": 0.3,
        },
      });

      mapRef.current.addLayer({
        id: "earthquakes-layer",
        type: "symbol",
        source: "earthquakes",
        layout: {
          "text-field": "●",
          "text-size": 15,
          "text-allow-overlap": true,
        },
        paint: {
          "text-color": "magenta",
        },
      });
    });

    // onclick
    mapRef.current.on("click", "earthquakes-layer", (e) => {
      // const coordinates = e.features[0].geometry.coordinates.slice();
      // console.log(coordinates);
      // while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
      //   coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
      // }
      console.log(window.screen);

      const point = e.point;
      const width = 20;
      const height = 20;
      const features = mapRef.current.queryRenderedFeatures(
        [
          [point.x - width / 2, point.y - height / 2],
          [point.x + width / 2, point.y + height / 2],
        ],
        { layers: ["earthquakes-layer"] },
      );

      setDataList(features);
      setOpen(true);
    });

    return () => mapRef.current.remove();
  }, []);

  const onClose = () => {
    setOpen(false);
  };

  return (
    <>
      <div
        style={{ height: "100%" }}
        ref={mapContainerRef}
        className="map-container"
      />
      <SimpleDialog open={open} onClose={onClose} dataList={dataList} />
    </>
  );
};

export default DialogTest;

function SimpleDialog(props) {
  const { onClose, open, dataList } = props;

  const handleClose = () => {
    onClose();
  };

  const handleListItemClick = (value) => {
    onClose(value);
  };

  return (
    <Dialog onClose={handleClose} open={open} maxWidth="sm" fullWidth={true}>
      <DialogTitle
        sx={{
          background: "#ebf3f1",
          margin: 0,
          padding: "10px",
          borderRadius: "3px 3px 0 0",
          fontWeight: "bold",
        }}
      >
        Report Lists
      </DialogTitle>
      <List sx={{ pt: 0 }}>
        {dataList.map((elem, idx) => (
          <ListItem disableGutters key={idx}>
            <ListItemButton>
              <ListItemAvatar>
                <Avatar sx={{ bgcolor: blue[100], color: blue[600] }}>
                  <DescriptionOutlinedIcon />
                </Avatar>
              </ListItemAvatar>
              <ListItemText primary={elem.properties.id} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </Dialog>
  );
}
