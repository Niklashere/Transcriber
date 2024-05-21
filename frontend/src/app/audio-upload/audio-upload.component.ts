import { Component } from '@angular/core';
import { AudioUploadService } from './audio-upload.service';

@Component({
  selector: 'app-audio-upload',
  templateUrl: './audio-upload.component.html',
  styleUrls: ['./audio-upload.component.css']
})
export class AudioUploadComponent {
  audioFile: File | null = null;
  language: string = '';
  whisperModel: string = '';
  chatgptModel: string = '';
  transcribedText: string = '';
  summarizedText: string = '';
  errorMessage: string = '';
  selectedFileName: string = 'Choose File';
  waitingForResult: boolean = false;

  constructor(private audioUploadService: AudioUploadService) { }

  onFileSelected(event: any) {
    this.audioFile = event.target.files[0];
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.selectedFileName = input.files[0].name;
    } else {
      this.selectedFileName = '';
    }
  }

  onSubmit() {
    this.waitingForResult = true;
    if (this.audioFile) {
      this.audioUploadService.uploadAudio(this.audioFile, this.language, this.whisperModel, this.chatgptModel).subscribe(
        response => {
          this.transcribedText = response['Transcribed Text'];
          this.summarizedText = response['Summarized Text'];
          this.errorMessage = '';
          this.waitingForResult = false;
        },
        error => {
          this.errorMessage = error;
          this.waitingForResult = false;
        }
      );
    }
  }
}
