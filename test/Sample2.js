// Set current layer and color
addLayer("MainLayer", "blue", "SOLID", RLineweight.Weight050);
setCurrentLayer("MainLayer");
setCurrentColor(new RColor(0, 0, 255));

// Start a transaction
startTransaction();

// Add some drawing entities
addLine([10, 10], [100, 10]);
addCircle([60, 60], 20);
addArc([60, 60], 30, 0, 90, false);
addSimpleText("Sample Text", [10, 90], 5, 0, "Arial", RS.VAlignTop, RS.HAlignLeft, false, false);

// End the transaction
endTransaction();
