

$(document).ready(function(){
    
    
  var endpoint = '/api/data'

  $.ajax({
      method:'GET',
      url:endpoint,
      success: function(data){
          console.log(data)


          var ctx = document.getElementById("line_1");
            var myLineChart = new Chart(ctx, {
                type: 'line',
                data : {
                    labels: data.date_chart,
                        
                    datasets: [
                    {
                        label: "Volume",
                        fill: !0,
                        lineTension: 0.5,
                        backgroundColor: "rgba(255, 255, 255, 0.2)",
                        borderColor: "#3C4CCF",
                        borderCapStyle: "butt",
                        borderDash: [],
                        borderDashOffset: 0,
                        borderJoinStyle: "miter",
                        pointBorderColor: "#3C4CCF",
                        pointBackgroundColor: "#fff",
                        pointBorderWidth: 1,
                        pointHoverRadius: 5,
                        pointHoverBackgroundColor: "#3C4CCF",
                        pointHoverBorderColor: "#3C4CCF",
                        pointHoverBorderWidth: 2,
                        pointRadius: 2,
                        pointHitRadius: 10,
                        data: data.volume_amount_chart,
                    },
                    ],
                },

                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                            }
                        }]
                    }
                }
            });

          
          var ctx = document.getElementById("bar");
            var myBarChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.date_chart,
                    
                    datasets: [
                      {
                        label: "Shares Bought",
                        backgroundColor: "#df5076",
                        borderColor: "#df5076",
                        borderWidth: 1,
                        hoverBackgroundColor: "#df5070",
                        hoverBorderColor: "#df5070",
                        data: data.volume_amount_chart,
                      },
                    ],
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });


            var ctx = document.getElementById("bar2");
            var myBarChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.date_chart,
                    
                    datasets: [
                      {
                        label: "Returns",
                        backgroundColor: "#5cc186",
                        borderColor: "#5cc186",
                        borderWidth: 1,
                        hoverBackgroundColor: "#5cc186",
                        hoverBorderColor: "#5cc186",
                        data: data.profit_chart,
                      },
                    ],
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });


      },


      
      error: function(error_data){
          console.log('error')
          //console.log(error_data)
      }

  })


});