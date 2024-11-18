import { useRef, useState } from "react";
import { Box, Typography, Drawer, Slider, Stack, Tooltip } from "@mui/material";
import Button from "@mui/material/Button";

const DrawerExample = () => {
  const [open, setOpen] = useState(false);

  const toggleDrawer = () => {
    setOpen(!open);
  };

  const [zoomState, setZoomState] = useState({
    clusterMaxZoom: {
      label: "Max zoom on which to cluster points ",
      min: 0,
      max: 22,
      val: 7,
      default: 7,
    },
    clusterMinPoints: {
      label: "Minimum number of points necessary to form a cluster",
      min: 1,
      max: 2000,
      val: 2,
      default: 2,
    },
    clusterRadius: {
      label: "Radius of each cluster",
      min: 0,
      max: 500,
      val: 50,
      default: 50,
    },
  });

  const saveSetting = () => {
    // TODO: save vals
    toggleDrawer();
  };

  const handleChange = (e, v) => {
    let p = { ...zoomState[e.target.name] };
    p.val = v;
    setZoomState({ ...zoomState, [e.target.name]: p });
  };

  const DrawerList = (
    <Box
      sx={{
        width: "100%",
        height: "100%",
        padding: 10,
        backgroundColor: "black",
      }}
    >
      <Typography variant="h4" color="common.white">
        Cluster setting
      </Typography>

      {Object.entries(zoomState).map(([name, elem]) => (
        <Box key={name + "-key"}>
          <Tooltip
            title={`${elem.min} to ${elem.max}`}
            componentsProps={{
              tooltip: {
                sx: {
                  bgcolor: "white",
                  color: "black",
                  fontSize: 12,
                },
              },
            }}
          >
            <Typography variant="h7" color="common.white">
              {elem.label}
            </Typography>
          </Tooltip>
          <Box>
            <Slider
              sx={{ width: "300px" }}
              name={name}
              defaultValue={elem.default}
              min={elem.min}
              max={elem.max}
              step={1}
              valueLabelDisplay="auto"
              onChange={handleChange}
            />
          </Box>
        </Box>
      ))}

      <Box sx={{ padding: 3 }}>
        <Stack spacing={5} direction="row">
          <Button variant="contained" onClick={saveSetting}>
            Save
          </Button>
          <Button variant="outlined" onClick={toggleDrawer}>
            Cancel
          </Button>
        </Stack>
      </Box>
    </Box>
  );

  return (
    <>
      <Button onClick={toggleDrawer}>Open drawer</Button>
      <div style={{ height: "100%", width: "100%" }}>
        <Stack direction="column">
          <Box> {zoomState.clusterMaxZoom.val}</Box>
          <Box> {zoomState.clusterMinPoints.val}</Box>
          <Box> {zoomState.clusterRadius.val}</Box>
        </Stack>
      </div>
      <Drawer
        PaperProps={{
          sx: { width: "600px" },
        }}
        open={open}
      >
        {DrawerList}
      </Drawer>
    </>
  );
};

export default DrawerExample;
