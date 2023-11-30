import React, { useRef, useEffect } from "react";

const DrawingCanvas = () => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const context = canvas.getContext("2d");

    // Add drawing logic here

    return () => {
      // Cleanup or remove event listeners if needed
    };
  }, []);

  return <canvas ref={canvasRef} width={400} height={400}></canvas>;
};

export default DrawingCanvas;
