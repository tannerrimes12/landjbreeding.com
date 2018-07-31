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

  $('.thumbnail-list a').each(function(index){
    if(index>3){
      $(this).css('display','none');
    }
    if(index==3){
      $(this).children('img').replaceWith('<div class="ellipsis-icon"><i class="fa fa-ellipsis-h"></i></div>');
    }
  });
});
