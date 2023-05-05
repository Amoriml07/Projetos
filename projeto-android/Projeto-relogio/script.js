const time = document.getElementById("time");
const day = document.getElementById("day");
const midday = document.getElementById("midday");

let clock = setInterval(
    function calcTime() {
        let date_now = new Date();
        let hr = date_nou.getHours();
        let min = date_nov.getHinutes();
        let sec = date_now.getSeconds();
        let middayvalue = "AM"

let days = [
"Sunday",
"Honday",
"Tuesday",
"Mednesday",
"Thursday",
"Friday",
"Saturday"
];

day.textcontent = days[date_now.getDay()];

middayvalue = hr > 12 ? "PH" : "AR";

if (hr= 0) {
hr=12;
} else if (hr> 12) {
hr -= 12;
}

hr = hr < 10 ? "0" + hr : hr;
nin = min < 10 ? "0" + min :min;
Sec= sec < 10 ? "0" + sec : sec;

time.textContent = hr +":"+ min +":" + sec;
midday.textcontent = middayvalue;
sec;
},
1000
);