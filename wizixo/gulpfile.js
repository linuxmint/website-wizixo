'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var browserSync = require('browser-sync').create();

var Paths = {
    TEMPLATE: './template',
    SCSS: 'template/assets/scss/**/*.scss',
    CSS: 'template/assets/css/',
    HTML: 'template/**/*.html'
}

// Compile sass into CSS
gulp.task('sass', function() {
    return gulp.src(Paths.SCSS)
      .pipe(sass.sync({
          outputStyle: 'expanded'   //nested, compact, expanded or compressed
      }).on('error', sass.logError)) 
      .pipe(gulp.dest(Paths.CSS))
      .pipe(browserSync.stream());
});

// Static Server
gulp.task('serve', function(done) {
    browserSync.init({
        server: Paths.TEMPLATE
    });
    done();
});

// watching scss/html files
gulp.task('watch', function(done) {
    gulp.watch(Paths.SCSS, gulp.series('sass'));
    gulp.watch(Paths.SCSS).on('change', browserSync.reload);
    gulp.watch(Paths.HTML).on('change', browserSync.reload);
    done();
});


gulp.task('default', gulp.series('sass', 'serve', 'watch'));