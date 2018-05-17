
$(function() {
  $(".list-group-item").click(function() {
    if($(this).hasClass('active')) {
      $(this).removeClass('active');
    }
    else {
      $(this).addClass('active');
    }
  });
});