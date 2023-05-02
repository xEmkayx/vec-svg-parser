// import parseInput from "./parse_text.js";
// import * as svg from "./create_js";
// const parseInput = require("./parse_text");
// const svg = require("./svg");
// Get references to DOM elements
const svgInput = document.getElementById("svg-input");
const renderBtn = document.getElementById("render-btn");
const svgContainer = document.getElementById("svg-container");

// Create new SVG element
let svgElement;
let svgMotherElement;
let screenSizeSet = false;
let currentColor = "black";

// Add event listener to render button
renderBtn.addEventListener("click", buttonClick);

function buttonClick(){
  const svgCode = svgInput.value;

  parse(svgCode);
  // console.log(svgMotherElement);

  // Add SVG code to SVG element

  // Clear SVG container and append new SVG element
  svgContainer.innerHTML = "";
  svgContainer.appendChild(svgMotherElement);
  console.log(svgMotherElement.outerHTML);
}

////////////////////////////////////////////////////////////////////////

function create(wdth, hght) {
  // Set SVG attributes
  if (!screenSizeSet){
      svgElement = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "g"
      );
      svgMotherElement = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "svg"
      );

    svgMotherElement.setAttribute("width", "100%");
    svgMotherElement.setAttribute("height", "100%");
    svgMotherElement.setAttribute("viewBox", `0 0 ${wdth + 50} ${hght}`);
    svgMotherElement.setAttribute("xmlns", "http://www.w3.org/2000/svg");
    svgMotherElement.setAttribute("version", "1.1");
    svgMotherElement.setAttribute("xmlns:xlink", "http://www.w3.org/1999/xlink");

    const translate = `translate(${wdth*0.1}, ${hght}) scale(1,-1)`;
    svgElement.setAttribute("transform", translate);
    screenSizeSet = true;
  }

}

function el(p, r1, r2){
    console.log("el");
    let x = p[0];
    let y = p[1];

    let ellipse = create_ellipse(x, y, r1, r2, "none", currentColor, 1);
    console.log("ellipse:");
  console.log(ellipse);
    svgElement.appendChild(ellipse);
}


function es(p, r1, r2, w1=0, w2=360){
let large_flac;// sweep_flag;
/*
  let large_flac = w2 - w1 > 180 ? 1 : 0;
*/
  let sweep_flag = r1 < 0 ? 0 : 1;
  if (w1 > w2){
    [w1, w2] = [w2, w1];
  }
  
  if (r1 < 0) r1 *= -1;

  let alle = ellipse_arc_points(p[0], p[1], r1, r2, w1, w2);
  let apx = alle[0];
  let apy = alle[1];
  let epx = alle[2];
  let epy = alle[3];

  // console.log(`Variablen es: ${apx} ${apy} ${epx} ${epy}`);
  sweep_flag = 1;
  large_flac = (w2 - w1 > 180 || w1 - w2 > 180) ? 1 : 0;

  let pt = create_path([apx, apy], [r1, r2], large_flac, sweep_flag, [epx, epy], currentColor);
  console.log("path:");
  console.log(pt);
  svgElement.appendChild(pt);
}

function finalize(){
  screenSizeSet = false;
  svgMotherElement.appendChild(svgElement);
  console.log("finalize: ");
  console.log(svgElement);
  // return svgElement;
}

function draw_line(x1, y1, x2, y2, line_width=1){
  svgElement.appendChild(create_line(currentColor, line_width, x1, y1, x2, y2));
}

function radians(degrees) {
  return degrees * (Math.PI / 180);
}

function ellipse_arc_points(x0, y0, a, b, theta1, theta2){
  theta1 = radians(theta1);
  theta2 = radians(theta2);

  function r(t) { return a * b / Math.sqrt((b * Math.cos(t)) ** 2 + (a * Math.sin(t)) ** 2); }
  function x(t) { return x0 + r(t) * Math.cos(t); }
  function y(t) { return y0 + r(t) * Math.sin(t); }

  let x1 = x(theta1);
  let y1 = y(theta1);
  let x2 = x(theta2);
  let y2 = y(theta2);

  return [x1, y1, x2, y2];
}

function parseInput(inpLines) {
      let lines = inpLines.split('\n');
      for (let idx = 0; idx < lines.length; idx++) {
        let i = lines[idx];
        i = i.trim();
        let a = i.split(' ');
        lines[idx] = a;
      }
    return lines;
  }

function parse(inpLines, outputFilename = "output.svg") {
  const lines = parseInput(inpLines);
  let previousCoords = [0, 0];

  console.log("parse");

  for (let idx = 0; idx < lines.length; idx++) {
    const line = lines[idx];

    switch (line[0].toLowerCase()) {
      case "os":
        // console.log("neues objekt");
        break;

      case "ob":
        const b = line[1].split(",");
        const width = parseFloat(b[2]) - parseFloat(b[0]);
        const height = parseFloat(b[3]) - parseFloat(b[1]);
        create(width, height);
        break;

      case "oe":
        if (idx + 1 === lines.length) {
          finalize();
          // paintercreate_finish(outputFilename);
          // return r
        }
        break;

      case "co":
        const c = parseInt(line[1].split(",")[0]);
        // console.log(`color: ${c}`);
        getColors(c);
        break;

      case "ma":
        const s = line[1].split(",");
        const x = parseFloat(s[0].trim());
        const y = parseFloat(s[1].trim());
        // console.log(`x: ${x} \t y: ${y}`);
        previousCoords = [x, y];
        break;

      case "da":
        const d = line[1].split(",");
        const x2 = parseFloat(d[0].trim());
        const y2 = parseFloat(d[1].trim());
        draw_line(previousCoords[0], previousCoords[1], x2, y2);
        previousCoords = [x2, y2];
        break;

      case "el":
        const rad = line[1].split(",");
        const x3 = parseFloat(rad[0].trim());
        const y3 = parseFloat(rad[1].trim());
        el([previousCoords[0], previousCoords[1]], x3, y3);
        previousCoords = [x3, y3];
        break;

      case "es":
        const rad2 = line[1].split(",");
        const w = line[2].split(",");
        const r1 = parseFloat(rad2[0].trim());
        const r2 = parseFloat(rad2[1].trim());
        const w1 = parseInt(w[0].trim());
        const w2 = parseInt(w[1].trim());
        es([previousCoords[0], previousCoords[1]], r1, r2, w1, w2);
        break;

      default:
        break;
        // console.log(0)
    }
  }
}

function getColors(c){
  let col;
  switch (c) {
    case 1:
        col = "black";
        break;
    case 2:
        col = "green";
        break;
    case 3:
        col = "red";
        break;
    case 4:
        col = "yellow";
        break;
    case 5:
        col = "blue";
        break;
    default: 
      col = "black";
    break;
  }

  currentColor = col;
}

// const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");

function create_ellipse(cx, cy, rx, ry, fill, stroke, strokewidth){
    let ellipseElement = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "ellipse"
      );

      ellipseElement.setAttribute("cx", cx);
      ellipseElement.setAttribute("cy", cy);
      ellipseElement.setAttribute("rx", rx);
      ellipseElement.setAttribute("ry", ry);
      ellipseElement.setAttribute("fill", fill);
      ellipseElement.setAttribute("stroke", stroke);
      ellipseElement.setAttribute("stroke-width", strokewidth + "px");

    return ellipseElement;
}

// function path(x1, y1, rx, ry, large_arc, counter_clockwise, x2, y2, stroke, fill, strokewidth, rot_x = 0){
function create_path(pos1, rad, large_arc, counter_clockwise, pos2, stroke,  rot_x = 0){
    let pathElement = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "path"
      );

    let x1 = pos1[0];
    let y1 = pos1[1];

    let x2 = pos2[0];
    let y2 = pos2[1];

    let rx = rad[0];
    let ry = rad[1];

    pathElement.setAttribute("d", `M ${x1}, ${y1} A ${rx}, ${ry} ${rot_x} ${large_arc}, ${counter_clockwise} ${x2}, ${y2}`);
    pathElement.setAttribute("stroke", stroke);
    pathElement.setAttribute("fill", 'none');
    pathElement.setAttribute("stroke-width", "1");
    
    return pathElement;
}

function create_line(stroke, strokewidth, x1, y1, x2, y2){
    let lineElement = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "line"
      );
    // self.__add_to_svg(self.templates["line"].format(stroke, strokewidth, y2, x2, y1, x1))

      lineElement.setAttribute("stroke", stroke);
      lineElement.setAttribute("stroke-width", strokewidth + "px");
      lineElement.setAttribute("stroke", stroke);
      lineElement.setAttribute("x1", x1);
      lineElement.setAttribute("y1", y1);
      lineElement.setAttribute("x2", x2);
      lineElement.setAttribute("y2", y2);
      return lineElement;
}

/*
function finalize(){
    
    return svg;
}
*/