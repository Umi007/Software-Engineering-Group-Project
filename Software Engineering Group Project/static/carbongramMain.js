


document.querySelector('#carbongramOnMind').addEventListener('click', e=>{
    document.querySelector('#createPostBody').style.display = "flex";
})

document.querySelector('#createPost').addEventListener('click', e=>{
    document.querySelector('#createPostBody').style.display = "flex";
})

document.querySelector('#carbongramHome').addEventListener('click', e=>{
    window.location.href = '/carbongram'
})


document.querySelector('#closeButton').addEventListener('click', e=>{
    document.querySelector('#createPostBody').style.display = "none";
})


for (const likeButton of document.querySelectorAll('.likeButton')){
        likeButton.addEventListener('click', e=>{
            animateIt(e)
        })
}

function animateIt(id){
  console.log(id)
}

function returnDel(){
    document.querySelector('#carbongramDeletePost').style.display = "none";
    document.querySelector('#carbongramChangeCover').style.display = "none";
    document.querySelector('#changeCoverBut').style.display = "none";
}


function deletePost(id){
        document.querySelector('#carbongramDeletePost').style.display = "flex";
        document.querySelector('#carbongramDeletePostId').value = id;
}

try {
  document.querySelector('#profileBackgroundCoverButton').addEventListener('click', e=>{
    document.querySelector('#carbongramChangeCover').style.display = "flex";
})


document.querySelector('#userProfilePic').onchange = evt => {
    const [file] = document.querySelector('#userProfilePic').files
     console.log(document.querySelector('#userProfilePic'))
         console.log("nice")

    var MaxSizeInBytes = 209715;
    if (file) {
        if( file && file.length === 1 && file.size > MaxSizeInBytes ){
          alert("The file size must be no more than " + parseInt(MaxSizeInBytes/1024/1024) + "MB");
          return;
        }
        document.querySelector('#changeCoverBut').style.display = "flex";
        document.querySelector('#carbongramChangeCoverImg').src = URL.createObjectURL(file)
    }
}

} catch (error) {
    console.error(error);
}

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        console.log(input)
        reader.onload = function (e) {
            $('#userProfilePic')
                .attr('src', e.target.result)
                .width(150)
                .height(200);
        };

        reader.readAsDataURL(input.files[0]);
    }
}


document.querySelector('#userpostimage').onchange = evt => {
    const [file] = document.querySelector('#userpostimage').files
    var MaxSizeInBytes = 209715;
    if (file) {
        if( file && file.length === 1 && file.size > MaxSizeInBytes ){
          alert("The file size must be no more than " + parseInt(MaxSizeInBytes/1024/1024) + "MB");
          return;
        }
        document.querySelector('#backgroundImages').src = URL.createObjectURL(file)
    }
}