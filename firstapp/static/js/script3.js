function checkAnswer()
{
    let selectAnswer = document.querySelector('input[name="answer"]:checked');
    let result=document.getElementById("result");
    if(selectAnswer === null)
    {
        result.innerText = "Please select an answer.";
        return;
    }
    let correctAnswer = "HTML";
    if(selectAnswer.value === correctAnswer)
    {
        result.innerText = "Correct answer!";
    }
    else
    {
        result.innerText = "Incorrect answer";
    }
}