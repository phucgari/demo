/**
 * Created by Administrator on 30/12/2016.
 */
function loadData() {
    console.log(">> LoadData");
    console.log("Loading data");
    $.ajax({
        type:"get",
        url: "/api/game",
        dataType:"json",
        contentType:"json",
        success:function(data){
            console.log(data);

            var dataListEl=document.getElementById("data-list");
            var h3Child=document.createElement("H3");
            for (var i=0 ; i<data.length; i+=1){
                console.log(i);
                var item = data[i];
                console.log(item.img);
                console.log(item.name);
                console.log(item._id)
                var gameImg=document.createElement("img");
                gameImg.src=item.img;
                dataListEl.appendChild(gameImg)

            }
        }
    })
}
function addData() {
    var gameName=document.getElementById("game-name").value;
    var gameDesc=document.getElementById("game-desc").value;
    var gameImg=document.getElementById("game-img").value;
    var gameLink=document.getElementById("game-link").value;
    var data={
        name: gameName,
        desc:gameDesc,
        img:gameImg,
        link:gameLink
    }
    $.ajax({
        url:"/api/game",
        type:"post",
        dataType:"json",
        contentType:"application/json",
        data: JSON.stringify(data),
        success: function (data) {
            console.log(data)
        }
    })
}
function deleteData() {
    var gameId=document.getElementById("game-id").value;
    $.ajax({
        url:"/api/game/"+gameId+"",
        type:"delete",
        success:function () {
            console.log('deleted')
        }
    })
}
function updateData() {
    var gameId=document.getElementById("game-id").value;
    var gameName=document.getElementById("game-name").value;
    var gameDesc=document.getElementById("game-desc").value;
    var gameImg=document.getElementById("game-img").value;
    var gameLink=document.getElementById("game-link").value;
    var data={
        name: gameName,
        desc:gameDesc,
        img:gameImg,
        link:gameLink
    }
    $.ajax({
        url:"/api/game/"+gameId+"",
        type:"put",
        dataType:"json",
        contentType:"application/json",
        data: JSON.stringify(data),
        success: function () {
            console.log('updated')

        }

    })
}