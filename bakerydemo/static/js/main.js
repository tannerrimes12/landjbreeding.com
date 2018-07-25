$(function(){
  console.log('attaching fancybox');
  $("a.gallery-image").fancybox();
});

$(document).ready(function()
{
    $(document).bind('contextmenu', function()
    {
        return false;
    });
});
