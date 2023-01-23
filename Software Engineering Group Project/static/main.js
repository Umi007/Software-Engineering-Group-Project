
try {
    document.querySelector('#profileButtonR').addEventListener('click', e => {
        document.querySelector('#profileDeleteCon').style.display = "none";
    })

    document.querySelector('#profileButtonB').addEventListener('click', e => {
        document.querySelector('#profileDeleteCon').style.display = "flex";
    })

    document.querySelector('.profileFormInput').addEventListener('keydown', e => {
        console.log(document.querySelectorAll('#profileFormInput'))
    })

var chosenBackground=0;
var index = 0;
for (const projectImg of document.querySelector('#profileBackgroundPreset').childNodes){
    if(projectImg.nodeName==="IMG") {
        projectImg.valueOf(index++)
        projectImg.addEventListener('click', e => {
            projectImg.setAttribute('style', 'height: 70px;border: 1px black solid;')

        })
    }
}

document.querySelector('#userProfilePic').onchange = evt => {
    const [file] = document.querySelector('#userProfilePic').files
    if (file) {
        document.querySelector('#profilePicture').src = URL.createObjectURL(file)
    }
}

document.querySelector('#userprofileBackground').onchange = evt => {

    const [file] = document.querySelector('#userprofileBackground').files
    var MaxSizeInBytes = 2097152;
    if (file) {
        console.log(file.size)
        if( file && file.length === 1 && file.size > MaxSizeInBytes ){
          alert("The file size must be no more than " + parseInt(MaxSizeInBytes/1024/1024) + "MB");
          return;
        }
        document.querySelector('.profile-main').style.backgroundImage = 'url('+URL.createObjectURL(file)+')';
        document.querySelector('#backgroundImages').src = URL.createObjectURL(file)
    }
}

document.querySelector('#userpostimage').onchange = evt => {
    console.log("nic4e")
    // const [file] = document.querySelector('#userpostimage').files
    // var MaxSizeInBytes = 209715;
    // if (file) {
    //     if( file && file.length === 1 && file.size > MaxSizeInBytes ){
    //       alert("The file size must be no more than " + parseInt(MaxSizeInBytes/1024/1024) + "MB");
    //       return;
    //     }
    //     console.log(document.querySelector('#backgroundImages').src)
    //     document.querySelector('#backgroundImages').src = URL.createObjectURL(file)
    // }
}


}catch (error) {
    console.log("error");
}

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#userProfilePic')
                .attr('src', e.target.result)
                .width(150)
                .height(200);
        };

        reader.readAsDataURL(input.files[0]);
    }
}


/*Button to scroll down page to specific element*/
$(window).scroll( function(){
  var header = $(window).scrollTop();
  var header = header * 1.5;
  var windowHeight = $(window).height();
  var position = header / windowHeight;
  position = 1 - position;
});


