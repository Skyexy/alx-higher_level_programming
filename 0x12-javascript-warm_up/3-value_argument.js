#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('No argument');
<<<<<<< HEAD
} else {
  process.argv.forEach((val, index) => {
    if (index > 2) {
      console.log(val);
    }
  });
=======
}else {
	process.argv.forEach((val, index) => {
		console.log(val[:3]);
	});
>>>>>>> 2ed8a1a9a0a888a3c05aa08cbd06756f0f0dd2ec
}
