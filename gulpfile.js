


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
   return gulp.src('app/static/public/*.css', { read: false })
     .pipe(gulprimraf());
});

gulp.task('compileCSS', ['cleanPublicCSS'], function () {
  return gulp.src('app/static/bundle.less')
    .pipe(less())
    //.pipe(md5())
    .pipe(csso())
    .pipe(gulp.dest('./app/static/public/'));
});

gulp.task('compileJS', function() {
  return gulp.src('app/static/main.js')
    .pipe(gulp.dest('./app/static/public/'));
});

gulp.task('releaseImages', function() {
  return gulp.src(['app/static/images/**/*']).pipe(gulp.dest('./static/dist/images'));
});

gulp.task('release', ['compileCSS', 'releaseImages'], function() {
	return gulp.src('app/static/public/*')
		//.pipe(zip('release.zip'))
		.pipe(gulp.dest('app/static/dist'));
});


gulp.task('watch', function () {
	console.log("Watch is active")
	gulp.watch(['app/static/**/*.js'], ['compileJS']);
    gulp.watch(['app/static/**/*.less'], ['compileCSS']);
});









