function getBotResponse(input) {
    //rock paper scissors
    if (input == "rock") {
        return "paper";
    } else if (input == "paper") {
        return "scissors";
    } else if (input == "scissors") {
        return "rock";
    }

    if (input == "how to generate summary") {
        return "log in, upload, generate. it's that easy!!";
    } else if (input == "what is this website") {
        return "This website allows you to upload long videos of lectures and converts them into short summary.";
    } else if (input == "scissors") {
        return "rock";
    }



    // Simple responses
    if (input == "hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else {
        return "Try asking something else!";
    }
}