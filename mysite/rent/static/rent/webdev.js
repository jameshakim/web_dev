$(".button-click a").on("click", function () {
    var $button = $(this);
    var txt = $button.closest("ul").prev().parent().find(".quantity");
    var oldValue = $(txt).val();

    if ($button.text() == "+") {
        var newVal = parseInt(oldValue) + 1;

    } else {
        if (oldValue > 0) {
            var newVal = parseInt(oldValue - 1);
        } else {
            newVal = 0;
        }
    }
    $(txt).val(newVal);
    calculate();
});

function calculate() {
    var total = 0;
    $('.button-click').each(function () {
        var amt = parseInt($(this).prev().val());
        var qty = parseInt($(this).parent().find(".quantity").val());
        total += (amt * qty);
    });
    $('#Amount').val(total.toFixed(2));
