import { useState, useRef } from "react";
import TextField from "@mui/material/TextField";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Accordion from "@mui/material/Accordion";
import AccordionActions from "@mui/material/AccordionActions";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import { DemoContainer } from "@mui/x-date-pickers/internals/demo";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { DatePicker } from "@mui/x-date-pickers/DatePicker";
import { fontGrid } from "@mui/material/styles/cssUtils";
import DeleteIcon from "@mui/icons-material/Delete";
import SearchIcon from "@mui/icons-material/Search";
import ClearAllIcon from "@mui/icons-material/ClearAll";
import { LogoDev } from "@mui/icons-material";

function DnDTest() {
  const [myWidth, setMyWidth] = useState(100);
  const div1ref = useRef(null);
  const div2ref = useRef(null);

  return (
    <>
      <Box sx={{ width: `${myWidth}px`, background: "red" }}>Box area</Box>
      <div ref={div1ref} style={{ width: "100px", background: "blue" }}>
        div area
      </div>
      <div
        id="divc"
        ref={div2ref}
        style={{ width: "100px", background: "yellow" }}
        onDragEnter={(event) => event.preventDefault()}
        onDragOver={(event) => event.preventDefault()}
        onDrop={(event) => {
          event.preventDefault();
          console.log("dropped !!");
        }}
      >
        div area (drop target)
      </div>
      <Button onClick={() => setMyWidth((prev) => prev + 10)}>button A</Button>
      <Button
        onClick={() => {
          div1ref.current.style.width = "200px";
          console.log(div1ref);
        }}
      >
        button B
      </Button>
      <Button
        draggable="true"
        onDragStart={(e) => {
          console.log("drag start");
          const img = new Image();
          img.src = "logo192.png";
          e.dataTransfer.setDragImage(img, 0, 0);
        }}
        onDragEnd={console.log("drag end")}
      >
        button C
      </Button>
    </>
  );
}

export default DnDTest;

