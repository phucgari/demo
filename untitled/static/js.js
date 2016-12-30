/**
 * Created by PC on 12/25/2016.
 */

var bachduong = ["Bạch Dương","năng động, sáng tạo, tiên phong, quyết đoán, mạnh mẽ, nhà lãnh đạo đầy tham vọng, hướng ngoại, cạnh tranh, nhiệt tình, tự lực, tự tin. Tuy nhiên hay nhanh nhẩu đoảng."];
var kimnguu = ["Kim Ngưu","cứng đầu, thận trọng, điềm tĩnh, kiên trì, lâu dài, hướng nội, bảo thủ, ổn định, siêng năng, đáng tin cậy, quan trọng vật chất, và thường có khả năng tài chính đáng kể."];
var songtu= ["Song Tử","thay đổi linh hoạt, nhạy bén, đa năng, sống động, tỉnh táo, khả năng giao tiếp, hòa đồng, khéo léo, nhanh nhẹn, trí tuệ, và tinh thần đầy tham vọng. Thích hợp với mọi ngành nghề"];
var cugiai = ["Cự Giải","sống nội tâm, nhạy cảm, u sầu, cảm thông, thận trọng, biết giữ bí mật, ỷ lại, bình tĩnh, trí tưởng tượng phong phú, tận tâm, và khá truyền thống."];
var sutu = ["Sư Tử","đầy tham vọng, một người yêu ánh đèn sân khấu,thích đầu cơ, hướng ngoại, lạc quan, đáng kính, trang nghiêm, tự tin, cởi mở, rực rỡ, lôi cuốn, kịch tính, cạnh tranh, có bản năng là một nhà lãnh đạo."];
var xunu = ["Xử Nữ","thực tế, có trách nhiệm, hay phân tích, phân biệt đối xử, lập kế hoạch cẩn thận, chính xác và đúng giờ, tận tụy, chủ nghĩa hoàn hảo, hay chỉ trích, có ý thức giữ gìn sức khỏe, và hơi hướng nội."];
var thienbinh = ["Thiên Bình","một sứ giả hòa bình,có tài ngoại giao, duyên dáng, tao nhã, lịch sự, đầu óc công bằng, hòa đồng, yêu nghệ thuật sáng tạo, thân thiện, hướng ngoại, và thường hơi thiếu quyết đoán."];
var thannong = ["Thần Nông","sâu sắc, mạnh mẽ, táo bạo, can đảm, bền vững, cạnh tranh, nhà nghiên cứu xuất sắc, tháo vát, thám tử tài ba, bí ẩn, sắc sảo, tự lực cánh sinh, trầm lặng, hướng nội."];
var nhanma = ["Nhân Mã","lạc quan, yêu tự do, giản dị, thân thiện, sôi động, thích giao du, nhiệt tình, hiếu học, nhìn xa trông rộng, thẳng thắn, trung thực, trung thành, hiếu động và thích du lịch."];
var maket = ["Ma Kết","đầy tham vọng, ý thức tổ chức tốt, kỷ luật, cứng nhắc, tiết kiệm, thận trọng, bảo thủ, có trách nhiệm, thiết thực, kiên trì, luôn xác định mục tiêu rõ ràng, có khả năng lên và sắp xếp kế hoạch tốt, thích hợp chính trị."];
var baobinh = ["Bảo Bình","chủ nghĩa cá nhân, không theo quy chuẩn, tư tưởng tiến bộ, độc đáo, độc lập, nhân đạo, vị tha, nhìn xa trông rộng, sâu sắc, trí tuệ, khéo léo, sáng tạo, không thể đoán trước, lúc thân thiện lúc hơi lánh đời."];
var songngu = ["Song Ngư","hay có những cảm giác khác thường, ấn tượng, yêu hoà bình, nghiêm trọng hóa vấn đề, thông cảm, từ bi, yêu nghệ thuật, thích sáng tạo mơ mộng, trí tưởng tượng phong phú, tận tụy, nhút nhát, sống nội tâm, quan trọng tinh thần, không quan trọng vật chất."];
var month=document.getElementById("month").value;
var day=document.getElementById("day").value;
function abc() {

    if (month == 3 && 21 <= day <= 31  || month == 4 && 1 <= day <= 19) {
        document.getElementById("name").innerHTML= bachduong[0];
        document.getElementById("des").innerHTML= bachduong[1];
    }
    if (month == 4 && 20 <= day <= 31  || month == 5 && 1 <= day <= 20) {
        document.getElementById("name").innerHTML = kimnguu[0];
        document.getElementById("des").innerHTML= kimnguu[1];
    }
    if (month == 5 && 21 <= day <= 31  || month == 6 && 1 <= day <= 21) {
        document.getElementById("name").innerHTML= songtu[0];
        document.getElementById("des").innerHTML= songtu[1];
    }
    if (month == 6 && 22 <= day <= 31  || month == 7 && 1 <= day <= 22) {
        document.getElementById("name").innerHTML= cugiai[0];
        document.getElementById("des").innerHTML = cugiai[1];
    }
    if (month == 7 && 23 <= day <= 31  || month == 8 && 1 <= day <= 22) {
        document.getElementById("name").innerHTML = sutu[0];
        document.getElementById("des").innerHTML= sutu[1];
    }
    if (month == 8 && 23 <= day <= 31  || month == 9 && 1 <= day <= 22){
        document.getElementById("name").innerHTML = xunu[0];
        document.getElementById("des").innerHTML= xunu[1];
    }
    if (month == 9 && 23 <= day <= 31  || month == 10 && 1 <= day <= 23) {
        document.getElementById("name").innerHTML = thienbinh[0];
        document.getElementById("des").innerHTML = thienbinh[1];
    }
    if (month == 10 && 24 <= day <= 31 || month == 11 && 22 <= day <= 19) {
        document.getElementById("name").innerHTML = thannong[0];
        document.getElementById("des").innerHTML = thannong[1]
    }
    if (month == 11 && 23 <= day <= 31 || month == 12 && 21 <= day <= 19) {
        document.getElementById("name").innerHTML = nhanma[0];
        document.getElementById("des").innerHTML = nhanma[1];
    }
    if (month == 12 && 22 <= day <= 31 || month == 1 && 1 <= day <= 19) {
        document.getElementById("name").innerHTML = maket[0];
        document.getElementById("des").innerHTML = maket[1];
    }
    if (month == 2 && 19 <= day <= 31  || month == 3 && 1 <= day <= 20) {
        document.getElementById("name").innerHTML = songngu[0];
        document.getElementById("des").innerHTML = songngu[1];
    }
    if (month == 1 && 20 <= day <= 31  || month == 2 && 1 <= day <= 18) {
        document.getElementById("name").innerHTML = baobinh[0];
        document.getElementById("des").innerHTML = baobinh[1];
    }
}
