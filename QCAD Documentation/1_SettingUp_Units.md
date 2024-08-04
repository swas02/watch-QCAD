
## Creating a New Document and Setting Units

To create a new document and set its unit of measurement, follow these steps:

### Script Example

```javascript
// Create a new document
var doc = createDocument();

// Define the unit you want to set
var unit = RS.Meter; // Use the correct unit code from the RS namespace

// Set the unit for the new document
doc.setUnit(unit);
```

### Available Units

Here are the common unit codes you can use:

- `RS.None` - No unit
- `RS.Inch` - Inches
- `RS.Foot` - Feet
- `RS.Mile` - Miles
- `RS.Millimeter` - Millimeters
- `RS.Centimeter` - Centimeters
- `RS.Meter` - Meters
- `RS.Kilometer` - Kilometers
- `RS.Microinch` - Microinches
- `RS.Mil` - Mils
- `RS.Yard` - Yards
- `RS.Angstrom` - Angstroms
- `RS.Nanometer` - Nanometers
- `RS.Micron` - Microns
- `RS.Decimeter` - Decimeters
- `RS.Decameter` - Decameters
- `RS.Hectometer` - Hectometers
- `RS.Gigameter` - Gigameters
- `RS.Astro` - Astronomical units
- `RS.Lightyear` - Lightyears
- `RS.Parsec` - Parsecs

## Working with an Existing Document

To work with the active document and set its unit of measurement:

### Script Example

```javascript
// Get the active document
var doc = getDocument(); // Use the correct method for getting the document

// Define the unit you want to set
var unit = RS.Meter; // Use the correct unit code from the RS namespace

// Set the unit for the active document
doc.setUnit(unit);
```