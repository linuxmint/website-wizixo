'use strict';

const gulp = require('gulp');
const sass = require('gulp-sass')(require('node-sass'));
const browserSync = require('browser-sync').create();

const Paths = {
  TEMPLATE: './dist',
  SCSS: './dist/assets/scss/**/*.scss',
  CSS: './dist/assets/css/',
  HTML: './dist/**/*.html'
};

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
        server: {
            baseDir: Paths.TEMPLATE,
            index: "mint-main.html"
        },
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