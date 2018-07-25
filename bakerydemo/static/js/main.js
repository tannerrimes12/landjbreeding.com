$(function(){
  console.log('attaching fancybox');
  $("a.gallery-image").fancybox({
    protect: true,
    buttons : [
      'zoom',
      'thumbs',
      'close'
    ]
  });

  $('.thumbnail-list').bind("contextmenu",function(e) {
    return false;
  });
});

// $(document).ready(function() {
//   $('.thumbnail-list').bind("contextmenu",function(e) {
//     return false;
//   });
// });
