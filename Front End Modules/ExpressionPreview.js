import React from "react";

const ExpressionPreview = ({ previewExpression }) => {
  return (
    <div>
      <h2>Expression Preview</h2>
      <p>{previewExpression}</p>
    </div>
  );
};

export default ExpressionPreview;
