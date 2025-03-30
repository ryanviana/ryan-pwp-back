import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { BlogPostModule } from './blog-post/blog-post.module';
import { WorkExperienceModule } from './work-experience/work-experience.module';
import { AchievementModule } from './achievement/achievement.module';
import { EducationModule } from './education/education.module';
import { SkillCategoryModule } from './skill-category/skill-category.module';
import { ProjectsModule } from './projects/projects.module';

@Module({
  imports: [
    MongooseModule.forRoot('mongodb://localhost:27017/personal-website'),
    BlogPostModule,
    WorkExperienceModule,
    AchievementModule,
    EducationModule,
    SkillCategoryModule,
    ProjectsModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
