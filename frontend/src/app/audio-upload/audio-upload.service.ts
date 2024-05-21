import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})

export class AudioUploadService {

  private apiUrl = 'http://localhost:8000/upload-audio/';

  constructor(private http: HttpClient) { }

  uploadAudio(audioFile: File, language: string, whisperModel: string, chatgptModel: string): Observable<any> {
    const formData: FormData = new FormData();
    formData.append('audiofile', audioFile);
    formData.append('language', language);
    formData.append('whisper_model', whisperModel);
    formData.append('chatgpt_model', chatgptModel);

    const headers = new HttpHeaders({
      'Accept': 'application/json'
    });

    return this.http.post(this.apiUrl, formData, { headers: headers })
      .pipe(
        catchError(this.handleError)
      );
  }

  private handleError(error: HttpErrorResponse) {
    return throwError(`Error: ${error.message}`);
  }
}
