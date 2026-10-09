function toggleInfo()
{
    var moreInfo = document.getElementById("more-info");
    var readMoreBtn = document.getElementById("readMoreBtn");

    if (moreInfo.style.display === "none") {
        moreInfo.style.display = "block";
        readMoreBtn.textContent = "Read Less";
    } else {
        moreInfo.style.display = "none";
        readMoreBtn.textContent = "Read More";
    }
}