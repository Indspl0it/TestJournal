// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawMoodChart);
google.charts.setOnLoadCallback(drawSentimentChart);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawMoodChart() {

  // Create the data table.
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Mood');
  data.addColumn('number', 'Days');
  data.addRows([
    ['Happy', 3],
    ['Sad', 1],
    ['Neutral', 2],
    ['Angry', 1],
    ['Excited', 2]
  ]);

  // Set chart options
  var options = {'title':'Mood Distribution',
                 'width':400,
                 'height':300};

  // Instantiate and draw our chart, passing in some options.
  var chart = new google.visualization.PieChart(document.getElementById('mood_chart_div'));
  chart.draw(data, options);
}

function drawSentimentChart() {

  // Create the data table.
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Sentiment');
  data.addColumn('number', 'Days');
  data.addRows([
    ['Positive', 5],
    ['Negative', 2],
    ['Neutral', 1]
  ]);

  // Set chart options
  var options = {'title':'Sentiment Distribution',
                 'width':400,
                 'height':300};

  // Instantiate and draw our chart, passing in some options.
  var chart = new google.visualization.PieChart(document.getElementById('sentiment_chart_div'));
  chart.draw(data, options);
}