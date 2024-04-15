// class Video {
//     constructor(title, uploader, time) {
//         this.title = title;
//         this.uploader = uploader;
//         this.time = time;
//     }

//     watch() {
//         console.log(`${this.uploader} watched all ${this.time} seconds of ${this.title}!`);
//     }
// }

// // Instantiate a new Video instance and call the watch() method
// const video1 = new Video("Funny Cats Compilation", "CatLover123", 300);
// video1.watch();

// // Instantiate a second Video instance with different values
// const video2 = new Video("Cooking Tutorial", "ChefMaster", 600);
// video2.watch();

// // Bonus: Use an array to store data for five Video instances
// const videoData = [
//     { title: "Gaming Highlights", uploader: "ProGamer", time: 480 },
//     { title: "Travel Vlog", uploader: "Wanderlust", time: 720 },
//     { title: "DIY Crafts", uploader: "CraftyCreator", time: 420 },
//     { title: "Fitness Workout", uploader: "FitLife", time: 900 },
//     { title: "Music Performance", uploader: "MusicMaestro", time: 360 }
// ];

// // Bonus: Loop through the array to instantiate those instances
// const videos = [];
// videoData.forEach(data => {
//     const video = new Video(data.title, data.uploader, data.time);
//     videos.push(video);
// });

// // Display information for each video
// videos.forEach(video => {
//     video.watch();
// });
