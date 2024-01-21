const trend_general = [['Year/Month', 'Excel', 'Power BI', 'Power Point', 'Python', 'R', 'SAS', 'SQL', 'Tableau'],
    ['2022-11', 841.0, 642.0, 146.0, 698.0, 520.0, 318.0, 1179.0, 624.0],
    ['2022-12', 1169.0, 923.0, 203.0, 971.0, 665.0, 396.0, 1686.0, 922.0],
    ['2023-01', 1279.0, 922.0, 373.0, 929.0, 581.0, 296.0, 2013.0, 1184.0],
    ['2023-02', 1045.0, 764.0, 232.0, 786.0, 475.0, 241.0, 1434.0, 725.0],
    ['2023-03', 987.0, 785.0, 189.0, 781.0, 493.0, 260.0, 1461.0, 714.0],
    ['2023-04', 849.0, 649.0, 188.0, 690.0, 437.0, 235.0, 1206.0, 680.0],
    ['2023-05', 708.0, 686.0, 145.0, 639.0, 395.0, 192.0, 1154.0, 651.0],
    ['2023-06', 763.0, 643.0, 182.0, 672.0, 384.0, 150.0, 1163.0, 693.0],
    ['2023-07', 770.0, 719.0, 219.0, 693.0, 447.0, 182.0, 1207.0, 643.0],
    ['2023-08', 964.0, 959.0, 239.0, 986.0, 597.0, 286.0, 1657.0, 861.0],
    ['2023-09', 967.0, 893.0, 249.0, 885.0, 596.0, 281.0, 1457.0, 834.0],
    ['2023-10', 1045.0, 843.0, 240.0, 944.0, 547.0, 261.0, 1493.0, 798.0],
    ['2023-11', 849.0, 725.0, 195.0, 829.0, 512.0, 235.0, 1301.0, 662.0],
    ['2023-12', 776.0, 644.0, 183.0, 675.0, 377.0, 223.0, 1111.0, 591.0]]

const via = [
    ['Site', 'Count', {role: 'annotation'}],
    ['via LinkedIn', 13059, 'LinkedIn'],
    ['via Upwork', 5852, 'Upwork'],
    ['via BeBee', 4456, 'BeBee'],
    ['via Trabajo.org', 2986, 'Trabajo'],
    ['via ZipRecruiter', 2283, 'ZipRecruiter'],
    ['via Indeed', 1558, 'Indeed'],
    ['via Snagajob', 846, ''],
    ['via Adzuna', 609, ''],
    ['via Jobs Trabajo.org', 518, ''],
    ['via Monster', 337, '']
]

const schedule = [
    ['Schedule type', 'Count'],
    ['Internship', 233],
    ['Full-time and Internship', 89],
    ['Full-time, Part-time, and Internship', 27],
    ['Part-time and Internship', 13],
    ['Temp work and Internship', 3]]

const intern_skill_general = [
    ['Technology', 'Count'],
    ['excel', 155],
    ['sql', 145],
    ['power_bi', 121],
    ['python', 107],
    ['r', 73],
    ['tableau', 71],
    ['powerpoint', 54],
    ['word', 29],
    ['sas', 28],
    ['spark', 22]]

const intern_last = [
    ['Technology', 'Count'],
    ['sql', 30],
    ['excel', 28],
    ['power_bi', 23],
    ['python', 19],
    ['powerpoint', 18],
    ['word', 16],
    ['sap', 13],
    ['qlik', 13],
    ['tableau', 9],
    ['sas', 7]
]

const intern_count = [
    ['Month', 'Count'],
    ['2022-11', 8],
    ['2022-12', 50],
    ['2023-01', 20],
    ['2023-02', 12],
    ['2023-03', 16],
    ['2023-04', 14],
    ['2023-05', 12],
    ['2023-06', 2],
    ['2023-07', 4],
    ['2023-08', 12],
    ['2023-09', 49],
    ['2023-10', 57],
    ['2023-11', 46],
    ['2023-12', 63]
]

const ide= [
    ['day', 'qlik', 'sap', 'spark', 'r'],
    ['2022-12-01', null, null, null, 7],
    ['2023-01-01', null, null, null, 4],
    ['2023-03-01', null, null, 2, null],
    ['2023-04-01', null, null, null, 1],
    ['2023-05-01', null, null, null, 7],
    ['2023-06-01', null, null, null, 1],
    ['2023-08-01', null, null, 8, 9],
    ['2023-09-01', null, null, 3, 7],
    ['2023-10-01', null, 2, 2, 18],
    ['2023-11-01', 1, 1, 1, 12],
    ['2023-12-01', 13, 13, 6, 7]
]



    document.addEventListener('DOMContentLoaded', function() {
        google.charts.load('current', {'packages':['corechart']});
        google.charts.setOnLoadCallback(drawChartListed);
    });

function drawChartListed() {
    let data = google.visualization.arrayToDataTable([
      ['Technology', 'Count'],
      ['sql', 19522],
      ['excel', 13012],
      ['python', 11178],
      ['power_bi', 10797],
      ['tableau', 10582],
      ['r', 7026],
      ['sas', 3556],
      ['powerpoint', 2983]
    ]);

    let options = {
      title: 'Top 8 most listed technologies',
      legend: 'none'
    };

    let chart = new google.visualization.ColumnChart(document.getElementById('top_8'));

      let data_trend_general = google.visualization.arrayToDataTable(trend_general)
  let options_trend_general = {
      title: 'Most listed technologies over time',
      legend: 'bottom'
  }

  let chart_trend_general = new google.visualization.LineChart(document.getElementById('trend'))

  chart_trend_general.draw(data_trend_general, options_trend_general)

    chart.draw(data, options);

  let data_intern = google.visualization.arrayToDataTable(schedule)
  let options_intern = {
          title: 'Intern Schedule',
          legend: 'none'
    }
    let chart_intern = new google.visualization.ColumnChart(document.getElementById('schedule'))
    chart_intern.draw(data_intern, options_intern)


    let data_via = google.visualization.arrayToDataTable(via)
      let options_via = {
          title: 'Sites with most job offers',
          legend: 'none'
      }
  let chart_via = new google.visualization.ColumnChart(document.getElementById('viad'))
  chart_via.draw(data_via, options_via)

    let last_intern_data =google.visualization.arrayToDataTable(intern_last)

    let last_intern_options = {
        title: 'Top Technologies for Interns in last month',
        legend: 'bottom',
    }

    let chart_intern_last = new google.visualization.ColumnChart(document.getElementById('last_intern'))
    chart_intern_last.draw(last_intern_data, last_intern_options)

    let data_general_skill =google.visualization.arrayToDataTable(intern_skill_general)

    let options_inetrn_general = {
        title: 'Top Technologies for Interns',
        legend: 'bottom'
    }

    let chart_intern_general = new google.visualization.ColumnChart(document.getElementById('gen_intern'))
    chart_intern_general.draw(data_general_skill, options_inetrn_general)

    let intern_trend = new google.visualization.arrayToDataTable(intern_count)

    let options_intern_trend = {
        title: 'Number of offers for internships',
        legend: 'bottom'
    }
    let chart_intern_trend = new google.visualization.LineChart(document.getElementById('intern_line'))
    chart_intern_trend.draw(intern_trend, options_intern_trend)

    let intern_trend_shift = new google.visualization.arrayToDataTable(ide)

    let options_intern_trend_shift = {
        title: 'Trend for tech of interest',
        legend: 'bottom',
        style: {
            0: {opacity: 0.3},
            1: {opacity: 0.3},
            2: {opacity: 0.3},
            3: {opacity: 0.3}
        }
    }
    let chart_intern_trend_shift = new google.visualization.LineChart(document.getElementById('last_tech'))
    chart_intern_trend_shift.draw(intern_trend_shift, options_intern_trend_shift)
}



