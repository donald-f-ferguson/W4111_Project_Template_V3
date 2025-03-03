import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { appConfig } from './app/app.config';
// you should not need to touch this file as all the configuration is done in app.config.ts
bootstrapApplication(AppComponent, appConfig).catch(err => console.error(err));
