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

  $('.thumbnail-list').each(function(){
    $(this).children('a').each(function(index){
      if(index>3){
        $(this).css('display','none');
      }
      if(index==3){
        $(this).children('img').attr('src', static_root +'img/elipses-icon.png');
      }

    });
  });
});
