print_ = document.getElementById("print_btn");

print_.onclick = (e) => {
    document.querySelector("#print_btn").style.display = "none";
    window.print();
    document.querySelector("#print_btn").style.display = "block";
}