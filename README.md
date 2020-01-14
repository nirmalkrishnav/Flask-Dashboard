1   Framework
--------------
For this app I have chosen an¬gular with material framework. Major reason for choosing angular was one,
Since the app is time critical, I did not want to use vanilla Js, jQuery also I didn’t want to lose  time on learning jinja right now.
Second is in the past one year I have been extensively using node + Angular for most of the projects. I want to leverage that.

I have used Bootstrap for layouts, High charts for visualization.
In the backend I have added Statistics package to perform few math operations on the dataset.


2   Design
----------

Dark mode is extensively used in this generation app for many reasons. One being enhancing readability and easy on the eyes. 
I have used the same dark theme throughout the application. Second being sleek material UI design with Roboto font.
The usability is accustomed to almost every user hence it reduces system learning time. 
Matching iconography that are relatable to the page/function. Flat color palette that are easy on the eyes.



3   Advantages
--------------

All data type corresponding to a Sensor, a Class label, or a Sample is uniformly colour coded.

Range filers within charts to triangulate to data shard.

Clearly depicts mean median and quartiles of the data sensor wise, class wise, sample wise - important factors of statistical analysis.

Easy option to compare between Sensors/ Samples side by side in one window.

Ease of access: The floating sidebars help user understand the context of the page and data. It is also.

easy to switch between pages/ sensors/ samples without much scroll.

Easy to access table depicting the whole dataset.

Leveraged Responsive and modern UI elements from both High charts Framework and material ex: range sliders, Zoom in capabilities.

Notification and sample run logs in UI to notify Backend ML Executions.

I have envisioned a scenario like the sensors are from a real steel production unit and developed the design for it. and charted out the diagram..

Used flat colour palette to be easy one the eyes that goes hand in hand with dark mode.

Useful metadata about data set and any sensor/ sample.

Extended all possible highcharts over the dataset.



4   To be Improved
-------------------

-   There is no click event written on chart. An important use case is on clicking on a chart point, example sensor3, the UI should be navigated 
    to that sensor page to display more information.

-   Customisable and changeable themes, colour palettes. Although colours are global vars set, but the UI function to change them is not implemented.

-   There is no Authentication and authorization on both front and backend code for this app. In critical data scenario, I would implement both 
    module level and URL authorization using route guards.
    
-   D3 chart integration to implement much more wide range of charts since right now it is hardcoded as Anomaly. Also, I would like to integrate
    dynamic sensor data into System Layout SVG chart.

-   Must implement App side or server-side caching of data, since I had to read multiple times for different pages.

-   Write stronger testcases to cover corner cases ex: changes in sensor names, data types etc., since the type of data is a known fact here, the 
    test cases are given weak priority.