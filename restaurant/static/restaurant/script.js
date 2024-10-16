
let special = document.getElementbyId("special_order") 
let shawarma = document.getElementById("shawarma_order")
let time = document.getElementById("time_estimation")
let error = document.getElementById("error")

let spec_condition = "{{order_today_special}}"
let shaw_condition = "{{meat}}"

console.log(spec_condition)
console.log(shaw_condition)

if (spec_condition) {
    special.style.display = 'block';
}
else {
    special.style.display = 'none';
}

if (shaw_condition) {
    shawarma.style.display = 'block';
}
else {
    shawarma.style.display = 'none';
}

if (!spec_condition && !shaw_condition) {
    special.style.display = 'none';
    shawarma.style.display = 'none';
    time.style.display = 'none';
    error.style.display = 'block';
}

