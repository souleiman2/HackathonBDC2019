console.log("succ")

window.onload = () => {
  console.log(document.getElementById("line-chart"))
  /*
  */

  new Chart(document.getElementById("line-chart"), {
    type: 'line',
    data: {
      labels: ['2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06', '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12', '2018-01', '2018-02', '2018-03', '2018-04', '2018-05', '2018-06', '2018-07', '2018-08', '2018-09', '2018-10', '2018-11', '2018-12', '2019-01'], 
      datasets: [{
          data: [3256, 4378, 5421, 6086, 6290, 4324, 4450, 5468, 5509, 5795, 5675, 3802, 4892, 5804, 5287, 6348, 5329, 4143, 4954, 3843, 3326, 3091, 2927, 2721, 3648],
          borderColor: "#3e95cd",
          label: "Page Views Each Month",
          fill: false
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'World population per region (in millions)'
      }
    }
  });
}
