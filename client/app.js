

//"CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"
function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var CRIM = document.getElementById("uiCRIM");
  var ZN = document.getElementById("uiZN");
  var INDUS = document.getElementById("uiINDUS");
  var CHAS = document.getElementById("uiCHAS");
  var NOX = document.getElementById("uiNOX");
  var RM = document.getElementById("uiRM");
  var AGE = document.getElementById("uiAGE");
  var DIS = document.getElementById("uiDIS");
  var RAD = document.getElementById("uiRAD");
  var TAX = document.getElementById("uiTAX");
  var PTRATIO= document.getElementById("uiPTRATIO");
  var B = document.getElementById("uiB");
  var LSTAT = document.getElementById("uiLSTAT");
  var estPrice = document.getElementById("uiEstimatedPrice");

  //"CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"
  var url = "http://127.0.0.1:5000/price_predictions"; 
  $.post(url, {
      CRIM: parseFloat(CRIM.value),
      ZN: parseFloat(ZN.value),
      //"CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"
      RM: parseFloat(RM.value),
      INDUS: parseFloat(INDUS.value),
      CHAS: parseFloat(CHAS.value),
      NOX: parseFloat(NOX.value),
      RM: parseFloat(RM.value),
      AGE: parseFloat(AGE.value),
      DIS: parseFloat(DIS.value),
      RAD: parseFloat(RAD.value),
      TAX: parseFloat(TAX.value),
      PTRATIO: parseFloat(PTRATIO.value),
      B: parseFloat(B.value),
      LSTAT: parseFloat(LSTAT.value),
  },function(data, status) {
      console.log(data.Predicted_price);
      estPrice.innerHTML = "<h2>" + data.Predicted_price.toString() + " Lakh</h2>";
      console.log(status);
  });
}



