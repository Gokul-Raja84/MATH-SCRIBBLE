import React, { useState } from "react";

const MathExpressionEditor = () => {
  const [expression, setExpression] = useState("");

  const handleInputChange = (event) => {
    setExpression(event.target.value);
  };

  const handleExpressionSubmit = () => {
    // Add logic to handle the submitted expression
    console.log("Submitted Expression:", expression);
  };

  return (
    <div>
      <textarea
        rows="3"
        cols="50"
        placeholder="Enter your mathematical expression here..."
        value={expression}
        onChange={handleInputChange}
      ></textarea>
      <br />
      <button onClick={handleExpressionSubmit}>Submit Expression</button>
    </div>
  );
};

export default MathExpressionEditor;
