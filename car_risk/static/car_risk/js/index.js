
const predict_car_risk = document.getElementById('predict_carrisk');


predict_car_risk.onclick = (event) => {
    document.querySelector(".car_result").style.display = "block";
}

// for print function 

const clicked = document.getElementById("print");

clicked.onclick = (e) => {
    window.print();
}