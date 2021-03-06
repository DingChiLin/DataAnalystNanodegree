## PISA Data Visualization - Compare Learning Time, Learning Achievement and ICT Resource of all PISA subjects for each Country

### Compatibility

The interaction functions is compatible with Chrome and Firefox browsers.

### Summary

This bubble chart describes the relationship between learning time and learning achievement of all the three PISA subjects (Math, Language, Science) in each country. The value in the x-axis is the learning time (min / week) and the value in the y-axis is the learning achievement Score (plausible value). Moreover, the different level of ICT (Information and Communications Technology) resource in each country is depicted using different depth of blue color, the higher the level, the deeper the color. Finally, users can highlight three countries they want to focus.

### Design

1. Initial Plot :

  - commit : 65bca06
  - plot : http://bl.ocks.org/DingChiLin/ef06010466f442261ec2a01da42acf01
  - design :
    1. Bubble chart: I use position to depict the main features, that is, the comparison of learning time and learning achievement between each country. Since I want to find out how much time students in each country spend in study and how well they perform. Than I can identify those students that can spend less time and get good perform and those in the contrast. Those special countries may lead us to some furthur studies and find out what's the main reason of achieving good academic performance.
    2. Sequential palette : I use color to compare the secondary feature - levels of ICT resource. The different depth of blue color correspond to different levels of it. Regarding to the above reason,I think ICT resource may be one of the reason that affect both the learnig time and learning achievement, so I use color to identify each level of ICT resource and see the trend of color change in the coordinate.
    3. Pre-attentive processing : I change the stroke of the circle of Chinese Taipei (my country) to red to highlight it and see its position compare to others clearer. Since I want to track and identify those interesting countries, so I choose a way to highlight it. Initially, I want to highlight it using different shape, but it will break the wholeness of the chart. So I choose stroke color as the pre-attentive object since it is intuitive, just like circle the point, and beautiful.

2. Second Plot :

  - commit : d806265 (with a little modification)
  -  plot : http://bl.ocks.org/DingChiLin/807355cffcbaccf5a5164fbf6902cdb5
  - design : the same as the initial sketch with little modifications and add more animation and interaction functions.
    1. Add Title and optimize the content and size of each label for readers.
    2. Move the achievement score to the y-axis and learning time to the x-axis since it makes more sense to put the independent variable (Learning Time) in the x-axis.
    3. Readers can choose the subjects (Math, Language, Science) which they are interested and see the bubble move when change subject.
    4. Readers can choose three countries to highlight and see the comparison between those chosen countries and others.

3. Third Plot :

  - commit : 09b8b99
  - plot : http://bl.ocks.org/DingChiLin/2e8551a0a8e4aa551a2b4b9686246d35
  - design :  the same as the second sketch with some modifications
    1. Change the radius of the bubble and the width of the strokes to make the highlight stroke clearer.
    2. Readers can open and close the color of ICT resource depending on whether they want to see it or not.
    3. Change the position of the buttons from the bottom to the right.

4. Final Plot :

  - commit : head
  - plot : http://bl.ocks.org/DingChiLin/c46e0ec94fcc2e8f8d8b4f3abade9d1d
  - design :  the same as the third sketch with some modifications
    1. Add an interactive function in the beginning to lead readers to follow my story.
    2. Remove "size" in tooltip.

### Feedback

1. After showing the initial sketch to my friends and colleagues, they give my some feedbacks:

  - Amy:
    1. No clear titles and labels.

  - Mark:
    1. The learning time variable should be in the x-axis since it is more like an independent variable, even though you're not doing a correlation analysis between the learning time and learning achievement, it is more comfortable for readers.
    2. There are three subjects in the PISA Test, can you create a select to let readers select which subject they want to see and move the bubble in plot when change subject? I want to see the difference of performances in each subject of one country.

  - Peter:
    1. I want to change the highlighted country, and I want to choose multiple countries at the same time, can you do that?

2. After showing the second sketch to my friends and colleagues, they give my some feedbacks:

  - Peter:
    1. It's a little misleading of the blue color of the ICT resource after adding the three highlight strokes since its color will affect the sense of color of the bubble itself.

  - Grace:
    1. The button should be put to the right blank area so I don't need to scroll up and down to change the setting and see the result. (He use Macbook-Pro 13 inch)

3. After submitting the project the first time:

  - Udacity reviewer:
    1. I need to tell readers my story, instead of just letting them to explore it by themselves.
    2. Remove the size value from tooltip

### Resources

1. Stephen Few - Practical Rules for Using Color in Charts : http://www.perceptualedge.com/articles/visual_business_intelligence/rules_for_using_color.pdf
2. Stephen Few - Designing Effective Tables and Graphs  : http://www.perceptualedge.com/articles/misc/Graph_Selection_Matrix.pdf
3. Dimple js - advanced examples : http://dimplejs.org/advanced_examples_index.html
4. PISA 2012 Taiwan Report : http://pisa.nutn.edu.tw/download/data/TaiwanPISA2012ShortReport.PDF
