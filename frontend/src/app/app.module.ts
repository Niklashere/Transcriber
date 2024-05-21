import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { AudioUploadComponent } from './audio-upload/audio-upload.component';
import { AudioUploadService } from './audio-upload/audio-upload.service';

import { ClipboardModule } from '@angular/cdk/clipboard';
import { ThemePalette } from '@angular/material/core';
import { ProgressBarMode, MatProgressBarModule } from '@angular/material/progress-bar';

@NgModule({
  declarations: [
    AppComponent,
    AudioUploadComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    ClipboardModule,
    MatProgressBarModule
    ],
  providers: [AudioUploadService],
  bootstrap: [AppComponent]
})
export class AppModule { }