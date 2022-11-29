#!/usr/bin/node
const wordy = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (let x = 0; x < wordy.length; x++) {
  console.log(''.concat(...wordy[x]));
}
