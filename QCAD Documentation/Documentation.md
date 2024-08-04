# QCAD Simple API Documentation

The QCAD Simple API in ECMAScript is designed to simplify common tasks related to drawing entities. This documentation provides an overview of the available functions in the API, their parameters, and usage examples. To use this API in your scripts, include the `simple.js` file.

```javascript
include("simple.js");
```

## Functions

- **`addArc(center, radius, startAngle, endAngle, reversed)`**
  Adds an arc to the drawing.

- **`addCircle(center, radius)`**
  Adds a circle to the drawing.

- **`addEntity(entity)`**
  Adds the given REntity to the drawing using layer and attributes as set by the entity.

- **`addLayer(name, colorName, linetypeName, lineWeight)`**
  Adds a layer to the drawing.

- **`addLine(startPoint, endPoint)`**
  Adds a line to the drawing.

- **`addObject(obj)`**
  Adds the given RObject to the drawing.

- **`addPoint(position)`**
  Adds a point to the drawing.

- **`addPolyline(points, closed, relative)`**
  Adds a polyline to the drawing.

- **`addShape(shape, color, linetype, lineweight)`**
  Adds the given RShape to the drawing as a new entity using current layer and attributes.

- **`addShapes(shapes)`**
  Adds the given RShapes to the drawing as new entities using current layer and attributes.

- **`addSimpleText(text, position, height, angle, font, vAlign, hAlign, bold, italic)`**
  Adds a simple text to the drawing.

- **`addSpline(points, closed)`**
  Adds a spline to the drawing.

- **`addXLine(startPoint, directionVector)`**
  Adds an infinite line to the drawing.

- **`autoZoom()`**
  Auto zoom.

- **`createDocument()`**
  Creates an (off-screen) document.

- **`createDocumentInterface()`**
  Creates an (off-screen) document with a document interface that can be used to import/export to/from files or graphics scenes and views.

- **`deleteObject(obj)`**
  Deletes the given RObject from the drawing.

- **`disableInput()`**
  Disables the main application window to prevent user input.

- **`enableInput()`**
  Enables the main application window to allow user input.

- **`endTransaction()`**
  Ends a transaction.

- **`getDocument()`**
  Returns the current RDocument or undefined.

- **`getDocumentInterface()`**
  Returns the current RDocumentInterface or undefined.

- **`getDouble(title, prompt, value, prec, lower, upper)`**
  Displays an input dialog box and returns a double.

- **`getGraphicsView()`**
  Returns the current or last active RGraphicsView.

- **`getInt(title, prompt, value, step, lower, upper)`**
  Displays an input dialog box and returns an integer.

- **`getIntersectionPoints(e1, e2, limited)`**
  Returns intersection points between the two given entities or shapes.

- **`getItem(title, prompt, items, idx, splitStr)`**
  Displays a combo drop-down box and returns item.

- **`getMainWindow()`**
  Returns a pointer to the main application window (RMainWindowQt).

- **`getOperation()`**
  Returns the current operation if we are in a transaction or a new operation.

- **`getText(title, prompt, txt)`**
  Displays an input dialog box and returns a string.

- **`getTransactionDocument()`**
  Returns the RDocument the current transaction applies to or the current document or undefined.

- **`getTransactionDocumentInterface()`**
  Returns the RDocumentInterface the current transaction applies to or the current document interface or undefined.

- **`hasLayer(name)`**
  Checks if the given layer exists.

- **`isInputEnabled()`**
  Returns true if user input is enabled.

- **`lengthen(entity, start, amount)`**
  Lengthens or shortens the given entity or shape.

- **`mirror(e, axis)`**
  Mirrors the given entity or shape at the given axis.

- **`move(e, offset)`**
  Moves the given entity or shape by the given offset.

- **`paste(docSource, diDestination, offset, scale, rotation, flipHorizontal, flipVertical, toCurrentLayer, overwriteLayers, overwriteBlocks)`**
  Pastes the given document into the current document or into the second given document.

- **`rotate(e, angle, center)`**
  Rotates the given entity or shape by the given angle around the given center.

- **`scale(e, factor, focusPoint)`**
  Scales the given entity or shape by the given factor with the given focus point.

- **`setCurrentColor(color)`**
  Sets the current color for newly added entities.

- **`setCurrentLayer(layerName)`**
  Sets the current layer to the given layer.

- **`sleep(d)`**
  Sleeps for the indicated time in milliseconds.

- **`startTransaction(d)`**
  Starts a transaction.

- **`trim(trimEntity, trimClickPos, limitingEntity, limitingClickPos, trimBoth)`**
  Trims the given entity/entities or shape(s).

- **`update()`**
  Keeps the user interface up to date during long operations.

- **`warning(msg)`**
  Prints a warning to stdout.

- **`zoomTo(p1, p2, p3, p4, p5)`**
  Zooms to the given entity.


## Functions in detail

---

### `addArc(center, radius, startAngle, endAngle, reversed)`

Adds an arc to the drawing.

**Parameters:**
- `center`: Center of the arc (e.g., `[cx, cy]` or `new RVector(cx, cy)`).
- `radius`: Radius of the arc.
- `startAngle`: Start angle of the arc in degrees.
- `endAngle`: End angle of the arc in degrees.
- `reversed`: Boolean indicating if the arc is reversed.

**Examples:**
```javascript
addArc([100, 100], 50, 0, 180, false);
addArc(new RVector(100, 100), 50, 0, 180, true);
```

---

### `addCircle(center, radius)`

Adds a circle to the drawing.

**Parameters:**
- `center`: Center of the circle (e.g., `[cx, cy]` or `new RVector(cx, cy)`).
- `radius`: Radius of the circle.

**Examples:**
```javascript
addCircle([50, 50], 20);
addCircle(new RVector(50, 50), 20);
```

---

### `addEntity(entity)`

Adds the given REntity to the drawing using layer and attributes as set by the entity.

**Parameters:**
- `entity`: The entity to be added.

**Examples:**
```javascript
var circle = new RCircle(new RVector(50, 50), 20);
addEntity(circle);
```

---

### `addLayer(name, colorName, linetypeName, lineWeight)`

Adds a layer to the drawing.

**Parameters:**
- `name`: Name of the layer.
- `colorName` (optional): Color name of the layer.
- `linetypeName` (optional): Line type of the layer.
- `lineWeight` (optional): Line weight of the layer.

**Examples:**
```javascript
addLayer("Layer1");
addLayer("Layer2", "red", "DASHED", RLineweight.Weight050);
```

---

### `addLine(startPoint, endPoint)`

Adds a line to the drawing.

**Parameters:**
- `startPoint`: Starting point of the line (e.g., `[x1, y1]` or `new RVector(x1, y1)`).
- `endPoint`: Ending point of the line (e.g., `[x2, y2]` or `new RVector(x2, y2)`).

**Examples:**
```javascript
addLine([0, 0], [100, 100]);
addLine(new RVector(0, 0), new RVector(100, 100));
```

---

### `addObject(obj)`

Adds the given RObject to the drawing.

**Parameters:**
- `obj`: The object to be added.

**Examples:**
```javascript
var point = new RPoint(new RVector(10, 10));
addObject(point);
```

---

### `addPoint(position)`

Adds a point to the drawing.

**Parameters:**
- `position`: Position of the point (e.g., `[x, y]` or `new RVector(x, y)`).

**Examples:**
```javascript
addPoint([10, 10]);
addPoint(new RVector(10, 10));
```

---

### `addPolyline(points, closed, relative)`

Adds a polyline to the drawing.

**Parameters:**
- `points`: Array of points where each point can be `[x, y]`, `[vector, bulge, relative]`, or `new RVector(x, y)`.
- `closed`: Boolean indicating if the polyline should be closed.
- `relative`: Boolean indicating if coordinates are relative to the previous point.

**Examples:**
```javascript
addPolyline([[0, 0], [100, 0], [100, 100], [0, 100]], true);
addPolyline([new RVector(0, 0), new RVector(100, 0), new RVector(100, 100), new RVector(0, 100)], true, true);
```

---

### `addShape(shape, color, linetype, lineweight)`

Adds the given RShape to the drawing as a new entity using current layer and attributes.

**Parameters:**
- `shape`: The shape to be added.
- `color` (optional): Color of the shape.
- `linetype` (optional): Line type of the shape.
- `lineweight` (optional): Line weight of the shape.

**Examples:**
```javascript
var rect = new RRectangle(new RVector(10, 10), new RVector(50, 50));
addShape(rect, new RColor(255, 0, 0), "CONTINUOUS", RLineweight.Weight050);
```



---

### `addShapes(shapes)`

Adds the given RShapes to the drawing as new entities using current layer and attributes.

**Parameters:**
- `shapes`: Array of shapes to be added.

**Examples:** [_*Correction needed_]
```javascript
// Add a Point
addShape(new RPoint(new RVector(0, 0)));

// Add a Line
addShape(new RLine(new RVector(0, 0), new RVector(10, 10)));

// Add an Arc
addShape(new RArc(new RVector(0, 0), 10, 0, Math.PI / 2));

// Add a Circle
addShape(new RCircle(new RVector(0, 0), 10));

// Add an Ellipse
addShape(new REllipse(new RVector(0, 0), 10, 5, 0));

// Add a Polyline
addShape(new RPolyline([
    new RVector(0, 0),
    new RVector(10, 0),
    new RVector(10, 10),
    new RVector(0, 10),
    new RVector(0, 0)
]));

// Add a Spline
addShape(new RSpline([
    new RVector(0, 0),
    new RVector(5, 10),
    new RVector(10, 0)
]));

// Add a Triangle (as a Polyline with 3 vertices)
addShape(new RPolyline([
    new RVector(0, 0),
    new RVector(10, 0),
    new RVector(5, 10),
    new RVector(0, 0)
]));

// Add an XLine
addShape(new RXLine(new RVector(0, 0), new RVector(1, 1)));

// Add a Ray
addShape(new RRay(new RVector(0, 0), new RVector(1, 1)));

// Add a Line with custom color, linetype, and lineweight
addShape(new RLine(new RVector(0, 0), new RVector(10, 10)), new RColor(255,0,0), "CONTINUOUS", 0.05);

```

---

### `addSimpleText(text, position, height, angle, font, vAlign, hAlign, bold, italic)`

Adds a simple text to the drawing.

**Parameters:**
- `text`: Text string.
- `position`: Position of the text (e.g., `[x, y]` or `new RVector(x, y)`).
- `height` (optional): Text height (default is `1`).
- `angle` (optional): Text angle in degrees (default is `0`).
- `font` (optional): Font name (default is `"standard"`).
- `vAlign` (optional): Vertical alignment (default is `RS.VAlignTop`).
- `hAlign` (optional): Horizontal alignment (default is `RS.HAlignLeft`).
- `bold` (optional): Boolean indicating if the text is bold (default is `false`).
- `italic` (optional): Boolean indicating if the text is italic (default is `false`).

**Examples:**
```javascript
addSimpleText("Hello World", [10, 10], 2, 0, "Arial", RS.VAlignTop, RS.HAlignLeft, false, false);
addSimpleText("Sample Text", new RVector(20, 20), 3, 45, "Courier", RS.VAlignMiddle, RS.HAlignCenter, true, true);
```

---

### `addSpline(points, closed)`

Adds a spline to the drawing.

**Parameters:**
- `points`: Array of fit points (e.g., `[x, y]` or `new RVector(x, y)`).
- `closed`: Boolean indicating if the spline is closed.

**Examples:**
```javascript
addSpline([[0, 0], [50, 100], [100, 0]], false);
addSpline([new RVector(0, 0), new RVector(50, 100), new RVector(100, 0)], true);
```

---

### `addXLine(startPoint, directionVector)`

Adds an infinite line to the drawing.

**Parameters:**
- `startPoint`: Starting point of the line (e.g., `[x, y]` or `new RVector(x, y)`).
- `directionVector`: Direction vector (e.g., `[dx, dy]` or `new RVector(dx, dy)`).

**Examples:**
```javascript
addXLine([0, 0], [1, 1]);
addXLine(new RVector(0, 0), new RVector(1, 1));
```

---

### `autoZoom()`

Automatically zooms to fit the drawing.

**Examples:**
```javascript
autoZoom();
```

---

### `createDocument()`

Creates an off-screen document.

**Returns:**
- A new empty `RDocument` with default settings.

**Examples:**
```javascript
var doc = createDocument();
```

---

### `createDocumentInterface()`

Creates an off-screen document with a document interface that can be used to import/export to/from files or graphics scenes and views.

**Returns:**
- A new empty `RDocumentInterface` with default settings.

**Examples:**
```javascript
var docInterface = createDocumentInterface();
```

---

### `deleteObject(obj)`

Deletes the given RObject from the drawing.

**Parameters:**
- `obj`: The object to be deleted.

**Examples:**
```javascript
var circle = new RCircle(new RVector(50, 50), 20);
addEntity(circle);
deleteObject(circle);
```

---

### `disableInput()`

Disables the main application window to prevent user input.

**Examples:**
```javascript
disableInput();
```

---

### `enableInput()`

Enables the main application window to allow user input.

**Examples:**
```javascript
enableInput();
```

---

### `endTransaction()`

Ends a transaction.

**Returns:**
- An `RTransaction` object containing information about the transaction.

**Examples:**
```javascript
startTransaction();
addLine([0, 0], [100, 100]);
endTransaction

();
```

---

### `getDouble(title, prompt, value, prec, lower, upper)`

Displays a dialog to input a double value.

**Parameters:**
- `title`: Title of the dialog box.
- `prompt`: Prompt text.
- `value` (optional): Default value (default is `0.0`).
- `prec` (optional): Precision (default is `1`).
- `lower` (optional): Minimum value (default is `-2147483647`).
- `upper` (optional): Maximum value (default is `2147483647`).

**Returns:**
- The input value.

**Examples:**
```javascript
var radius = getDouble("Input Radius", "Enter the radius of the circle:", 10, 2, 1, 100);
addCircle([50, 50], radius);
```

---

### `getDocument()`

Returns the current `RDocument` or `undefined`.

**Returns:**
- The current `RDocument` or `undefined`.

**Examples:**
```javascript
var doc = getDocument();
```

---

### `getDocumentInterface()`

Returns the current `RDocumentInterface` or `undefined`.

**Returns:**
- The current `RDocumentInterface` or `undefined`.

**Examples:**
```javascript
var docInterface = getDocumentInterface();
```

---

### `getGraphicsView()`

Returns the current or last active `RGraphicsView`.

**Returns:**
- The current or last active `RGraphicsView`.

**Examples:**
```javascript
var view = getGraphicsView();
```

---

### `getMainWindow()`

Returns a pointer to the main application window (`RMainWindowQt`).

**Returns:**
- A pointer to the main application window.

**Examples:**
```javascript
var mainWindow = getMainWindow();
```

---

### `lengthen(entity, start, amount)`

Lengthens or shortens the given entity or shape.

**Parameters:**
- `entity`: Entity to lengthen or shorten.
- `start`: Boolean indicating if extending at the start point (`true`) or end point (`false`).
- `amount`: Amount to lengthen or shorten (negative values shorten).

**Examples:**
```javascript
var line = new RLine(new RVector(0, 0), new RVector(100, 100));
addEntity(line);
lengthen(line, true, 50);
```

---

### `mirror(entity, axis)`

Mirrors the given entity or shape at the specified axis.

**Parameters:**
- `entity`: Entity to mirror.
- `axis`: Axis of mirroring (e.g., `[x1, y1, x2, y2]` or `new RLine(x1, y1, x2, y2)`).

**Examples:**
```javascript
var line = addLine(0, 0, 100, 100);
mirror(line, [0, 50, 100, 50]);
```

---

### `move(entity, offset)`

Moves the given entity or shape by the given offset.

**Parameters:**
- `entity`: Entity to move.
- `offset`: Offset (e.g., `[x, y]` or `new RVector(x, y)`).

**Examples:**
```javascript
var circle = addCircle(0,0,10);
move(circle, [10, 10]);
```
<!-- 
---

### `paste(docSource, diDestination, offset, scale, rotation, flipHorizontal, flipVertical, toCurrentLayer, overwriteLayers, overwriteBlocks)`

Pastes the given document into the current or specified document.

**Parameters:**
- `docSource`: Source document to paste.
- `diDestination`: Destination document (`undefined` for current document).
- `offset`: Offset (e.g., `[x, y]` or `new RVector(x, y)`).
- `scale`: Scaling factor.
- `rotation`: Rotation angle in degrees.
- `flipHorizontal`: Boolean to flip horizontally.
- `flipVertical`: Boolean to flip vertically.
- `toCurrentLayer`: Boolean to paste all entities to the current layer.
- `overwriteLayers`: Boolean to overwrite existing layers.
- `overwriteBlocks`: Boolean to overwrite existing blocks.

**Examples:**
```javascript
var docSource = createDocument();
addCircle([50, 50], 20);
var docDestination = getDocument();
paste(docSource, docDestination, [10, 10], 1, 0, false, false, false, false, false);
``` -->

---

### `rotate(entity, angle, center)`

Rotates the given entity or shape by the specified angle around the center point.

**Parameters:**
- `entity`: Entity to rotate.
- `angle`: Angle in degrees.
- `center`: Center of rotation (e.g., `[x, y]` or `new RVector(x, y)`).

**Examples:**
```javascript
var line = addLine(0, 0, 100, 100);
rotate(line, 45, [50, 50]);
```

---

### `scale(entity, factor, focusPoint)`

Scales the given entity or shape by the given factor with the specified focus point.

**Parameters:**
- `entity`: Entity to scale.
- `factor`: Scaling factor.
- `focusPoint`: Focus point of scaling (e.g., `[x, y]` or `new RVector(x, y)`).

**Examples:**
```javascript
var circle = addCircle([50, 50], 20);
scale(circle, 1.5, 50, 50);
```

---

### `setCurrentColor(color)`

Sets the current color for newly added entities.

**Parameters:**
- `color`: Color (e.g., `new RColor(255, 0, 0)` or color value).

**Examples:**
```javascript
setCurrentColor(new RColor(255, 0, 0));
addCircle([50, 50], 20);
```

---

### `setCurrentLayer(layerName)`

Sets the current layer to the specified layer.

**Parameters:**
- `layerName`: Name or ID of the layer.

**Examples:**
```javascript
setCurrentLayer("Layer1");
addCircle([50, 50], 20);
```

---

### `startTransaction(document)`

Starts a transaction for adding multiple entities.

**Parameters:**
- `document`: `RDocument` or `RDocumentInterface` to apply the transaction to (defaults to current document).

**Examples:**
```javascript
startTransaction();
addLine([0, 0], [100, 100]);
addCircle([50, 50], 20);
endTransaction();
```

---

### `update()`

Keeps the user interface up to date during long operations.

**Examples:**
```javascript
update();
```



---

### `sleep(d)`

**Description:**  
Sleeps for the indicated time in milliseconds.

**Parameters:**
- `d` (int): The duration in milliseconds to sleep.

**Usage Example:**
```cpp
sleep(500); // Sleep for 500 milliseconds
```


---

### `trim(trimEntity, trimClickPos, limitingEntity, limitingClickPos, trimBoth)`

**Description:**  
Trims the given entity/entities or shape(s).

**Parameters:**
- `trimEntity` (Entity): The entity or shape to be trimmed.
- `trimClickPos` (Point): The click position to start the trim operation.
- `limitingEntity` (Entity): The limiting entity or shape to constrain the trim.
- `limitingClickPos` (Point): The click position to determine the trim limit.
- `trimBoth` (bool): Specifies whether to trim both sides or just one.

**Usage Example:**
```cpp
trim(myLine, clickPosition1, boundaryLine, clickPosition2, true);
```


---

### `warning(msg)`

**Description:**  
Prints a warning message to stdout.

**Parameters:**
- `msg` (string): The warning message to print.

**Usage Example:**
```cpp
warning("This is a warning message!");
```

---

---

### `zoomTo(p1, p2, p3, p4, p5)`

**Description:**  
Zooms to the given entity.

**Parameters:**
- `p1` (Point): The first point for zooming.
- `p2` (Point): The second point for zooming.
- `p3` (Point): The third point for zooming.
- `p4` (Point): The fourth point for zooming.
- `p5` (Point): The fifth point for zooming.

**Usage Example:**
```cpp
zoomTo(point1, point2, point3, point4, point5);
```

---

---

### `getInt(title, prompt, value, step, lower, upper)`

**Description:**  
Displays an input dialog box and returns an integer.

**Parameters:**
- `title` (string): The title of the input dialog.
- `prompt` (string): The prompt message displayed in the dialog.
- `value` (int): The default value to display in the input field.
- `step` (int): The step size for increasing/decreasing the value.
- `lower` (int): The minimum allowable value.
- `upper` (int): The maximum allowable value.

**Returns:**
- (int): The integer value entered by the user.

**Usage Example:**
```cpp
int userInput = getInt("Input Required", "Enter a number:", 10, 1, 0, 100);
```

---

---

### `getText(title, prompt, txt)`

**Description:**  
Displays an input dialog box and returns a string.

**Parameters:**
- `title` (string): The title of the input dialog.
- `prompt` (string): The prompt message displayed in the dialog.
- `txt` (string): The default text to display in the input field.

**Returns:**
- (string): The string value entered by the user.

**Usage Example:**
```cpp
string userInput = getText("Input Required", "Enter your name:", "Default Name");
```
--
Certainly! Here’s a documentation example for the `saveDocument()` function you provided. This documentation includes an overview, description of parameters, return values, and usage examples.

---
## Save Document in QCAD

This document provides details on how to use the `Save` action in QCAD to save a document programmatically. The provided code snippet demonstrates how to create a `Save` action, specify the file path, format version, and handle file overwriting.

## Code Overview

The code snippet demonstrates the following steps:
1. **Creating a Save Action**
2. **Specifying File Details**
3. **Saving the Document**

```javascript
// Create an instance of the Save action
var saveAction = new Save();

// Specify the path where the file should be saved
var fileName = "path/to/your/file.dxf"; // Replace with the actual file path

// Specify the file format version (e.g., AutoCAD 2013)
// This can be adjusted based on the desired format compatibility
var fileVersion = "AutoCAD 2013";

// Enable or disable overwrite warnings
// `true` means that if a file already exists at the specified path,
// the user will be prompted to confirm overwriting
var overwriteWarning = true;

// Call the save method to save the document
// Parameters:
// - `fileName`: The path and name of the file to save
// - `fileVersion`: The file format version to use
// - `overwriteWarning`: Whether to show warnings about overwriting existing files
var success = saveAction.save(fileName, fileVersion, overwriteWarning);

// `success` will be `true` if the save operation was successful, `false` otherwise
```
---

## Sample Script

Here is a complete sample script that demonstrates the use of various API functions:

```javascript
include("simple.js");

// Create a new document and interface
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

// Initialize Save action
var saveAction = new Save();

// Define the file path and other parameters
var fileName = "path/file2.dxf";
var fileVersion = ""; // Use empty string to let QCAD decide the format
var overwriteWarning = true; // Show overwrite warning if file exists

// Attempt to save the document
var success = saveAction.save(fileName, fileVersion, overwriteWarning);


```

This script demonstrates the creation of a new document, adding layers, setting colors, drawing entities, and updating the user interface. Adjust the parameters and functions to fit your specific drawing needs.