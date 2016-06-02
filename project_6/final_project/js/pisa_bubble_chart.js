function Chart(){

  var myChart;
  var subjectList = ['Math', 'Language', 'Science']
  var splitData = []
  var thisObj = this
  var story_step;

  thisObj.reservedColors = ['rgb(74, 162, 74)', 'rgb(237, 156, 41)', 'rgb(197, 52, 48)']

  thisObj.init = function(data){

    // set step to be 1 and hide the control panel
    story_step = 1
    story(story_step)

    var svg = dimple.newSvg("#chart-container", '100%', '100%');

    // Title
    svg.append("text")
       .attr("x", 90)
       .attr("y", 70)
       .attr("text-anchor", "left")
       .style("font-size", "25px")
       .style("font-weight", "bold")
       .text("Learning Time vs Score : ")

    svg.append("text")
       .attr("x", 390)
       .attr("y", 70)
       .attr("text-anchor", "left")
       .attr("id", "title-subject")
       .style("font-size", "25px")
       .style("font-weight", "bold")
       .text(subjectList[0])

    // Parse Data
    for(var s_index in subjectList){
      splitData[s_index] = []
      for(var index in data){
        splitData[s_index][index] = {}
        splitData[s_index][index]['Country'] = data[index]['Country']
        splitData[s_index][index]['ICTResourcesClass'] = data[index]['ICTResourcesClass']
        splitData[s_index][index]['LearningTime'] = data[index][subjectList[s_index] + 'LearningTime']
        splitData[s_index][index]['Score'] = data[index][subjectList[s_index] + 'Score']
        splitData[s_index][index]['Size'] = 10

        if(s_index==0){ // set the selecor option only once
          $('#highlight-country-selector .selectpicker').append($('<option>', {
            value: data[index]['Country'],
            text: data[index]['Country']
          }))
        }
      }
    }

    // Default Select
    $('.selectpicker').selectpicker('refresh');
    $('#country-select-green').selectpicker('val', ['China-Shanghai'])
    $('#country-select-yellow').selectpicker('val', ['Vietnam'])
    $('#country-select-red').selectpicker('val', ['Qatar'])

    // Set ICT Switch Button
    $(".ict-checkbox").bootstrapSwitch();
    $('.ict-checkbox').on('switchChange.bootstrapSwitch', function (event, state) {
      updateICTColor(state)
    })

    // ICT Resource Legend
    svg.append("text")
       .attr("x", 600)
       .attr("y", 70)
       .attr("text-anchor", "left")
       .attr("id", "ict-title")
       .style("font-size", "15px")
       .style("font-weight", "bold")
       .text("ICT Resource (A:highest ~ E:lowest)")

    // Main Chart
    myChart = new dimple.chart(svg)
    myChart.setBounds(90, 130, 800, 600)

    // Score
    var x = myChart.addMeasureAxis("x", "LearningTime")
    x.overrideMin = 100
    x.overrideMax = 400
    x.title = 'Learning Time ( min / week )'
    x.fontSize = "20"

    // Learning Time
    var y = myChart.addMeasureAxis("y", "Score")
    y.overrideMin = 360
    y.overrideMax = 600
    y.title = 'Score (plausible value)'
    y.fontSize = "20"

    // Size
    var z = myChart.addMeasureAxis("z", "Size")
    z.overrideMin = 5
    z.overrideMax = 27

    // Group
    var s = myChart.addSeries(["Country", "ICTResourcesClass"], dimple.plot.bubble)
    s.stacked = false
    s.addOrderRule(['ICTResourcesClass'], true)
    s.getTooltipText = function (e) {
      console.log(e)
      return [
        "Country: " + e.aggField[0],
        "ICT Level: " + e.aggField[1]
      ]
    }

    myChart.addLegend(560, 90, 300, 20, "right")

    updateData(splitData[0])
    updateICTColor(false)
  }

  // Next Step
  this.nextStep = function(){
    story_step += 1
    story(story_step)
  }

  // The Contents of the story
  function story(step){
    var text;

    switch(step){
      case 1:
        text = "This bubble chart is made based on the PISA 2012 survey data, \
                which shows the relation between learning time and learning achievement \
                in math of each country (or district). <br><br>\
                From this chart, we can see there is no significant relation \
                between learning time and achievement in general, \
                but we can find some special countries from this map"
        break
      case 2:
        text = "Students in Korea (green stroke) spend time less than \
                most of the countries but perform very well ( rank fifth ). \
                However, Students in Chile (red stroke) spend far more time \
                on learning but perform not quite well."
        updateHighlightCountry('korea', thisObj.reservedColors[0])
        updateHighlightCountry('chile', thisObj.reservedColors[2])
        updateICTColor(false)
        break
      case 3:
        text = "Add one more variable - ICT resource and look again. \
                This variable shows the information and communication technology resource \
                students have in each country. <br><br> \
                I split it into five level from A to E, \
                A means the highest and E the lowest. With the help of technology, \
                students may spend less time on learning and get better achievement. <br><br>\
                In this chart we can see, generally, \
                the higher the ICT resource a country have, the better their students perform, \
                which may explain some of the achievement gaps between Korea and Chile. \
                However, there are still some exceptions."
        updateICTColor(true)
        break
      case 4:
        text = "Let's look at some countries which don't follow the general trend. <br><br>\
                Students in China Shanghai (green) perform best but only have C-level ICT resource. <br><br>\
                Students in Qatar (red) have highest ICT resource but still perform poorly, \
                in the contrast, \
                students in Vietnam (orange) have lowest ICT resource but perform not bad. <br><br>\
                Educational researchers may take further research at these particular countries \
                and see which variables have a greater impact on performance."
        updateHighlightCountry('china-shanghai', thisObj.reservedColors[0])
        updateHighlightCountry('vietnam', thisObj.reservedColors[1])
        updateHighlightCountry('qatar', thisObj.reservedColors[2])
        break
      case 5:
        text = "Now, you can choose the countries you are interested in to highlight \
                and open or close the ICT resource color hue on your own. <br><br>\
                Moreover, since there are three subjects in the PISA research (Math, Language, Science), \
                you can choose to look the other two subjects and adjust all the variables mentioned above. \
                <br><br> Good luck :)"
        break
      default:
        $('#pida-data-story').hide()
        $('#pida-control-panel').show()

    }

    $('#story-content p').html(text)

  }

  thisObj.changeSubject = function(index){
    $('#title-subject').text(subjectList[index])
    updateData(splitData[index])
  }

  thisObj.changeHighlightCountry = function(id, color){
    var country = $("#" + id + " option:selected").text()
    updateHighlightCountry(parseCountryName(country), color)
  }

  function parseCountryName(name){
    return name.toLowerCase().replace(/\(|\)|\ /g, "-")
  }

  // Change the subject data
  function updateData(data){
    myChart.data = data

    myChart.assignColor("A", "#063870", "#063870", 0.9);
    myChart.assignColor("B", "#0D51B0", "#0D51B0", 0.9);
    myChart.assignColor("C", "#3188E8", "#3188E8", 0.9);
    myChart.assignColor("D", "#6CB0F8", "#6CB0F8", 0.9);
    myChart.assignColor("E", "#B3D9FD", "#B3D9FD", 0.9);

    myChart.draw(1000)
  }

  // Change the highlight country
  function updateHighlightCountry(country, color){
    myChart.series[0].afterDraw = function (s, d) {
      if(s.style.stroke == color && s.id.indexOf(country) == -1){
        d3.select(s)
          .style('stroke', s.style.fill)
          .style('stroke-width', '5px')

      }

      if(s.id.indexOf(country) > -1){
        d3.select(s)
          .style('stroke', color)
          .style('stroke-width', '5px')

      }
    }

    myChart.draw()
  }

  // open and close the ICT color hue
  function updateICTColor(is_ict){
    myChart.series[0].afterDraw = function (s, d) {
      if(is_ict){ // open

        $('.dimple-legend').show()
        $('#ict-title').show()

        var level = d.key.split('/')[1][0]
        var color

        // five ICTlevel
        switch(level){
          case 'A':
            color = "#063870"
            break
          case 'B':
            color = "#0D51B0"
            break
          case 'C':
            color = "#3188E8"
            break
          case 'D':
            color = "#6CB0F8"
            break
          case 'E':
            color = "#B3D9FD"
            break
        }

        d3.select(s)
          .style('fill', color)
          .attr('opacity', 0.9)

        if(thisObj.reservedColors.indexOf(d3.select(s).style('stroke')) == -1 ){
          d3.select(s)
           .style('stroke', color)
        }

      }else{ // close
        $('.dimple-legend').hide()
        $('#ict-title').hide()

        d3.select(s)
          .style('fill', '#808080')
          .attr('opacity', 0.6)

        if(thisObj.reservedColors.indexOf(d3.select(s).style('stroke')) == -1 ){
          d3.select(s)
            .style('stroke', '#808080')
        }
      }
    }
    myChart.draw(1)
  }

}

var chart = new Chart();

