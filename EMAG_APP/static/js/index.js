$('#searchForm').on('shown.bs.collapse', function () {
    // focus input on collapse
    $("#search").focus()
})
AOS.init();
$(document).on("click", ".confirm-delete", function() {
    $("#confirmDeleteModal").attr("caller-id", $(this).attr("id"));
});

$(document).on("click", "#confirmDeleteEventModal", function() {
    var caller = $("#confirmDeleteEventModal")
        .closest(".modal")
        .attr("caller-id");
    window.location = `/delete/event/${caller}`;
});

$(document).on("click", "#confirmDeleteProjectModal", function() {
    var caller = $("#confirmDeleteProjectModal")
        .closest(".modal")
        .attr("caller-id");
    window.location = `/delete/project/${caller}`;
});

$(document).on("click", "#confirmDeleteAchModal", function() {
    var caller = $("#confirmDeleteAchModal").closest(".modal").attr("caller-id");
    window.location = `/delete/ach/${caller}`;
});

$(function() {
    var cat = $("#select").attr("category");
    $("#select").val(cat).attr("selected", "selected");
});
