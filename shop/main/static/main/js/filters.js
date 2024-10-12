$(document).ready(function() {
    $("#filterButton").click(function() {
        $("#filters").toggle();
        $(this).text($(this).text() === "Фильтры" ? "Скрыть фильтры" : "Фильтры");
    });
});

