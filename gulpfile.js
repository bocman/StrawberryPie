


var gulp = require('gulp'),
	less = require('gulp-less'),
	path = require('path'),
	csso = require('gulp-csso'),
	rev = require('gulp-rev'),
	uglify = require('gulp-uglify'),
	watch = require('gulp-watch');

gulp.task('test', function() {
	console.log("nisem ne ");
});


gulp.task('compileCSS', function () {
  var quoteSrc = './static/public/*.css'

  return gulp.src('./static/*.less')
    .pipe(less({
        paths: [ path.join(__dirname, 'less', 'includes') ]
    }))
    .pipe(rev())
    .pipe(csso())
    //.pipe(rimraf("./static/public/*.css"))
    .pipe(gulp.dest('./static/public/'));
});

gulp.task('compileJS', function() {
  return gulp.src('lib/*.js')
    .pipe(uglify())
    .pipe(gulp.dest('dist'));
});