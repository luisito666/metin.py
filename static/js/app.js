;(function (){

  let sticky = false
  let currentPosition = 0

  const imageCounter = $("[data-name='image-counter']").attr('content')

  console.log(imageCounter);

  $('#sticky-navigation').removeClass('hidden')
  $('#sticky-navigation').slideUp(0)

  setInterval(()=> {

    if (currentPosition < imageCounter) {
      currentPosition++
    } else {
      currentPosition = 0
    }

    $("#gallery .inner").css({
      left: "-"+currentPosition*100+"%"
    })


  }, 3000)

  $(window).scroll(() => {
    const inBottom = isInBottom()

    if (inBottom && !sticky) {
      // Mostrar la navegación
      sticky = true
      stickNavigation()
    } 
    if (!inBottom && sticky) {
      // Ocultar la navegación
      sticky = false
      unStickNavigation()
    }

  })

  function stickNavigation() {
    sticky = true;
    $('#description').addClass('fixed').removeClass('absolute')

    $('#navigation').slideUp('fast')
    $('#sticky-navigation').slideDown('fast')
  }

  function unStickNavigation() {  
    sticky = false;
    $('#description').removeClass('fixed').addClass('absolute')

    $('#navigation').slideDown('fast')
    $('#sticky-navigation').slideUp('fast')
  }

  function isInBottom() {
    const $description = $('#description')
    const descriptionHeight = $description.height()

    return $(window).scrollTop() > $(window).height() - descriptionHeight * 2
  }

})()