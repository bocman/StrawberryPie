


var gulp = require('gulp'),
	less = require('gulp-less'),
	path = require('path'),
	csso = require('gulp-csso'),
	uglify = require('gulp-uglify'),
	watch = require('gulp-watch');
	md5 = require('gulp-md5'),
	gulprimraf = require('gulp-rimraf'),
	zip = require('gulp-zip');
	copy = require('gulp-copy');

gulp.task('test', function() {
	console.log("nisem ne ");
});

gulp.task('cleanPublicCSS', function () {
   return gulp.src('./static/public/*.css', { read: false })
     .pipe(gulprimraf());
});

gulp.task('compileCSS', ['cleanPublicCSS'], function () {
  return gulp.src('./static/bundle.less')
    .pipe(less())
    //.pipe(md5())
    .pipe(csso())
    .pipe(gulp.dest('./static/public/'));
});

gulp.task('compileJS', function() {
  return gulp.src('./static/main.js')
    .pipe(gulp.dest('./static/public/'));
});

gulp.task('releaseImages', function() {
  return gulp.src(['./static/images/**/*']).pipe(gulp.dest('./static/dist/images'));
});

gulp.task('release', ['compileCSS', 'releaseImages'], function() {
	return gulp.src('./static/public/*')
		//.pipe(zip('release.zip'))
		.pipe(gulp.dest('./static/dist'));
});


gulp.task('watch', function () {
	console.log("Watch is active")
	gulp.watch(['./static/**/*.js'], ['compileJS']);
    gulp.watch(['./static/**/*.less'], ['compileCSS']);
});









