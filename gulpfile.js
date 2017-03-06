/**
 * Created by xiezhigang on 17/3/6.
 */
const gulp = require("gulp");
const sourcemaps = require("gulp-sourcemaps");
const uglify = require("gulp-uglify");
const concat = require("gulp-concat");
const cleanCss = require("gulp-clean-css");
const htmlReplace = require("gulp-html-replace");
const del = require("del");
const rev = require("gulp-rev");
const collector = require("gulp-rev-collector");

