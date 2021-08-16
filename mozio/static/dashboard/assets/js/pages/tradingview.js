

const chartProperties = {
    width:1000,
    height:400,
    timescale:{
        timeVisible:true,
        secondsVisible:false,
    }
}
$(document).ready(function(){
    var endpoint = '/api/data'

    $.ajax({
        method:'GET',
        url:endpoint,
        success: function(data){
            
            const domElement = document.getElementById('tvchart');

            const chart = LightweightCharts.createChart(domElement, chartProperties);
            const candleSeries = chart.addCandlestickSeries();
            const cdata = data.map(d => {
                return {time:d[0]/1000,open:parseFloat(d[1]).toFixed(4),high:parseFloat(d[2]).toFixed(4),low:parseFloat(d[3]).toFixed(4),close:parseFloat(d[4]).toFixed(4)}
            });
            candleSeries.setData(cdata);

        }
    })
    
})