// Themes begin
am4core.useTheme(am4themes_dark); // Use dark theme

// Set primary color to Netflix red (#E50914)
am4core.colors.list = [am4core.color("#E50914"), am4core.color("#000000")]; // Set primary and secondary colors

am4core.useTheme(am4themes_animated);
// Themes end

var chart = am4core.create("right", am4charts.PieChart3D);
chart.hiddenState.properties.opacity = 0; // this creates initial fade-in

chart.legend = new am4charts.Legend();
chart.legend.labels.template.fill = am4core.color("#ffffff"); // Set legend label color to white

chart.data = data;

var series = chart.series.push(new am4charts.PieSeries3D());
series.dataFields.value = "total";
series.dataFields.category = "type";
series.slices.template.propertyFields.fill = "color";
series.labels.template.fill = am4core.color("#ffffff"); // Set data label color to white

